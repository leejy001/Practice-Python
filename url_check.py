import re

def main():
    p = re.compile('^http[s]*://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

    url = input()

    print(p.match(url) != None)

main()
