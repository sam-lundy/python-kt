

pattern = r"BGP neighbor is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}), remote AS \d+, internal link\n\s+BGP state = Established"
matches = re.findall(pattern, output)

for match in matches:
    print(match)