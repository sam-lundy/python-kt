from netmiko import ConnectHandler
import argparse
import csv
import json
import sys
import xmltodict
import getpass
import sqlite3
import logging
import traceback
from nested_lookup import nested_lookup

def check_cli_args():
    parser = argparse.ArgumentParser(
        description = "Get configuration from the devices"
    )
    parser.add_argument(
        '-i', '--input_list', type=str, help='Input CSV device list', required=True
    )
    args = parser.parse_args()
    return args


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def loadcsv(inputfile):
    with open (inputfile, mode='r') as infile:
        reader = csv.reader(infile)
        data = list(reader)
    header = data[0]
    all_device_dict = []
    for row in data[1:]:
        device_dict = {}
        for i, entry in enumerate(row):
            device_dict[header[i]] = entry
        all_device_dict.append(device_dict)
    return all_device_dict

def determinetype(hostname):
    if '-MGMT-' in hostname or '-MGMTCAE-' in hostname:
        type = 'MGMT'
    elif '-R2MGMT-' in hostname or '-R2COR-' in hostname or '-R2-' in hostname:
        type = 'R2'
    elif '-R1-' in hostname:
        type = 'R1'
    elif '-R0-' in hostname:
        type = 'R0'
    elif '-COR-' in hostname or '-CORCAE-' in hostname or '-R2CAE-' in hostname or '-R1CAE-' in hostname or '-R0CAE' in hostname or '-ISILCAE-' in hostname:
        type = 'COR'
    else:
        type = 'unknown'
    return type

def determinecred(type):
    cred = {}
    if type == "COR":
        cred = {'username':'AUTOCORRO', 'password' : 'KaOACM$OPqSam7S844XJ4'}
    if type == "MGMT":
        cred = {'username':'AUTOMGMTRO', 'password' : '5q$InWxJy6gmmb9H9q13d'}
    if type == "R2":
        cred = {'username':'AUTOR2RO', 'password' : 'Y7HuI$V5PmwVcVZ7icjUV'}
    if type == "R1":
        cred = {'username':'AUTOR1RO', 'password' : 'uTh74Ujo$f4UFxBOFa8Y$'}
    if type == "R0":
        cred = {'username':'AUTOR0RO', 'password' : 'OrNiwEl9JJF$wTZ7HN7WE'}
    if type == "unknown":
        print("Unable to determine the password from device name")
        cred = {'username':'unknown', 'password' : 'unknown'}
    return cred

def main():
    args = check_cli_args()
    DLIST = args.input_list
    all_device = loadcsv(DLIST)
    cred = {}
    for device in all_device:
        if '#' in device['hostname']:
            continue
        type = determinetype(device['hostname'])
        cred = determinecred(type)
        # cred = {'username':'AUTOR2RO', 'password' : 'Y7HuI$V5PmwVcVZ7icjUV'}
        # cred["username"] = input("Username:")
        # cred["password"] = getpass.getpass()
        connect = {**device, **cred}
        hostname = connect['hostname']
        del connect['hostname']
        try:
            print("Trying connect to " + device['hostname'])
            net_connect = ConnectHandler(**connect)
            net_connect.find_prompt()
        except:
            traceback.print_exc()
            print("Unable to connect to " + device['hostname'])
            continue
        try:
            tl0 = net_connect.send_command("terminal length 0")
            output = net_connect.send_command("show run")
            filename = hostname + ".txt"
            with open(filename, 'w') as f:
                f.write(output)
            print("Collected configuration from" + device['hostname'])
        except:
            print("Unable to get configuration from" + device['hostname'])
            traceback.print_exc()
            continue
        net_connect.disconnect()

if __name__ == "__main__":
    main()