# Create an application which connects to a site and pulls out all links, or images, and saves them to a
# list. *Optional: Organize the indexed content and don't allow duplicates. Have it put the results into an easily searchable index
# file.*

import sys, urllib2, re

def getLinks(url):
    page = urllib2.urlopen(url).read()
    res = ""
    links = re.findall(r"<a href=\"([\w_\/-]*)\">",page)
    for link in sorted(links):
        if re.match("http[s]?://",link):
            res += link+"\n"
        else:
            res += url+link+"\n"
    with open("pagelinks.txt","w") as f:
        f.write(res[:-1])

def main():
    getLinks(sys.argv[1])

if __name__ == "__main__": 
    main()