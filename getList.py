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

                problems = re.findall(r"\*\*(.+)\*\*\s-\s(.+)",f)
                for idx,problem in enumerate(problems):
                    problems[idx] = (re.sub('[^\w\s]', '', problem[0]),problem[1])
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

def createPyFiles():
    categories = getProjects()
    for category in sorted(categories):
        for project in categories[category]:
            lower = project[0].lower()
            fname = "".join(word[0].upper()+word[1:] for word in lower.split())
            loc = "./"+category+"/"+fname[0].lower()+fname[1:]
            createGenericFile(loc+".py",project[1])

def createComment(string,lineLength):
    words = re.findall(r"[^\s]+",string)
    res = ""
    lines = [words[i:i+lineLength] for i in range(0,len(words),lineLength)]
    for line in lines:
        res += "# "+" ".join(line)+"\n"
    return res[:-1]

def createGenericFile(loc,comments):
    f = open(loc,"w")
    f.write(createComment(comments,20)+"\n\nimport sys, os \n\ndef main():\n    # Code here\n\nif __name__ == \"__main__\": \n    main()")

def main():
    createList()
    # createPyFiles()

if __name__ == "__main__":
    main()