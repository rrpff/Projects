import sys, os, re

def getProjects():
    categories = {}
    fullList = []
    for dirname, dirnames, filenames in os.walk("."):
        for filename in filenames:
            checkFilename = re.match("README.md",filename)
            if checkFilename:
                f = open(os.path.join(dirname,filename),"rU").read()
                getCategory = re.match(r"(\w+[\s\w]*)\n----",f)
                category = getCategory.group(1)

                problems = re.findall(r"\*\*([\w|\s]+)\*\*\s-\s(.+)",f)
                categories[category] = sorted(problems)
    return categories

def createList():
    categories = getProjects()
    string = ""
    for category in sorted(categories):
        string += "\n##"+category+"\n"
        for project in categories[category]:
            string += "[ ] **"+project[0]+"** - "+project[1]+"\n\n"
    f = open("list.md","w")
    f.write(string)

def main():
    createList()

if __name__ == "__main__":
    main()