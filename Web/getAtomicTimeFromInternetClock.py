# This program will get the true atomic time from an atomic time clock on the Internet. Use any one of
# the atomic clocks returned by a simple Google search.

import sys,urllib2,re

def getTime():
    page = urllib2.urlopen("http://time.is/").read()
    time = re.search("<div id=\"twd\">([0-9:]+)",page)
    return time.group(1)

def main():
    print "The time is "+getTime()+"."

if __name__ == "__main__": 
    main()