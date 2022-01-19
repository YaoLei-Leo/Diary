##To insert new post to the specific part and recent posts
import re
import sys
import os
import logging
logging.basicConfig(level=logging.NOTSET)

def CheckExistence(syntaxList, user):
    cardSyntaxList = syntaxList[1]
    
    try:
        if re.search(r'<p class="author">(.*)</p>', cardSyntaxList[0]).group(1) != user:
            logging.error("The article name and user is not right with your input")
            sys.exit()
    except IndexError:
        logging.error("No article in this user page")
        sys.exit()

def ExtractMarkdownAndCardSyntaxToList(html):
    markdownSyntaxList = list()
    cardSyntaxList = list()
    otherSyntaxList = list()
    otherSyntax = ''
    with open(html) as f:
        for line1 in f:
            if re.search(r'<!-- Markdown insert position -->', line1):
                otherSyntax = otherSyntax + line1
                otherSyntaxList.append(otherSyntax)
                otherSyntax = ''
                    
                for line2 in f:
                    if re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', line2):
                        markdownSyntaxList.append(line2)
                    else:
                        otherSyntax = otherSyntax + line2
                        break
    
            elif re.search(r'<!-- Card insert position -->', line1):
                otherSyntax = otherSyntax + line1
                otherSyntaxList.append(otherSyntax)
                otherSyntax = ''

                for line2 in f:
                    if re.search(r'<!-- Card insert end position -->', line2):
                        otherSyntax = otherSyntax + line2
                        break
                    cardSyntax = line2
                    for i in range(1, 10):
                        line2 = f.readline()
                        cardSyntax = cardSyntax + line2
                    cardSyntaxList.append(cardSyntax)
            else:
                otherSyntax = otherSyntax + line1
        otherSyntaxList.append(otherSyntax)
    # print(markdownSyntaxList)
    # print(cardSyntaxList)
    # print(otherSyntaxList[2])
    return [markdownSyntaxList, cardSyntaxList, otherSyntaxList]

def ModifyExistPost(syntaxList, articleName, user, md, img, hashTag, abstract):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    found = 0
    for i in range(len(cardSyntaxList)):
        if re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', cardSyntaxList[i]) and re.search(r'<p class="author">(.*)</p>', cardSyntaxList[i]).group(1) == user:
            found = 1
            ID = re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', cardSyntaxList[i]).group(1)
            originalImg = re.search(r'<img src="(.*)">', cardSyntaxList[i]).group(1)
            originalHashTag = re.search(r'<p class="hashTag">(.*)</p>', cardSyntaxList[i]).group(1)
            originalAbstract = re.search(r'<p class="abstractContent">(.*)</p>', cardSyntaxList[i]).group(1)
            if img != "" and img != originalImg:
                # print(originalImg)
                # print(img)
                cardSyntaxList[i] = cardSyntaxList[i].replace(originalImg, img)
                logging.info("Img src was changed")
            if hashTag != "" and hashTag != originalHashTag:
                cardSyntaxList[i] = cardSyntaxList[i].replace(originalHashTag, hashTag)
                logging.info("Hash tag was changed")
            if abstract != "" and abstract != originalAbstract:
                cardSyntaxList[i] = cardSyntaxList[i].replace(originalAbstract, abstract)
                logging.info("Abstract was changed") 
            if md != "":
                if md[-1] != "/":
                    for i in range(len(markdownSyntaxList)):
                        if re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i]).group(2) == ID:
                            originalMd = re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i]).group(1)
                            print(md)
                            print(originalMd)
                            if md != originalMd:
                                markdownSyntaxList[i] = markdownSyntaxList[i].replace(originalMd, md)
                                logging.info("Markdown src was changed")
        if found == 0:
            logging.error("This article does not exist in this user page!")
            sys.exit()

    return [markdownSyntaxList, cardSyntaxList, otherSyntaxList]            
    
def WriteSyntaxToHtml(syntaxList, htmlPath):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    output = open(htmlPath, 'w')
    
    output.write(otherSyntaxList[0])
    for i in markdownSyntaxList:
        output.write(i)
    output.write(otherSyntaxList[1])
    for i in cardSyntaxList:
        output.write(i)
    output.write(otherSyntaxList[2])

def main(articleName, user, md, img, hashTag, abstract):
    img = md.replace(".md","_src/") + img

    # 1. User folder
    html = "../{}/{}".format(user, user) + '.html'
    output = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    CheckExistence(syntaxList, user)
    syntaxList = ModifyExistPost(syntaxList, articleName, user, md, img, hashTag, abstract)
    WriteSyntaxToHtml(syntaxList, output)
    
    # 2. Recent posts
    md = "./{}/{}".format(user, md)
    html = '../index.html'
    output = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    syntaxList = ModifyExistPost(syntaxList, articleName, user, md, img, hashTag, abstract)
    WriteSyntaxToHtml(syntaxList, output)

if __name__ == "__main__":
    articleName = "Test Insertion"
    user = "JaneNote"
    
    md = ""
    img = ""
    hashTag = "#test modification3"
    abstract = "Test modification3"
    
    main(articleName, user, md, img, hashTag, abstract)