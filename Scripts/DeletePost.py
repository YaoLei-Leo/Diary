##To delete a post in the user folder and recent posts.
import re
import sys
import os
import logging
logging.basicConfig(level=logging.NOTSET)

def CheckExistence(syntaxList, user):
    cardSyntaxList = syntaxList[1]
    
    try:
        if re.search(r'<p class="author">(.*)</p>', cardSyntaxList[0]).group(1) != user:
            logging.error("The user is not equal to your inputted user, check your HTML file.")
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

def DeletePosts(syntaxList, articleName, user):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    found = 0
    for i in cardSyntaxList:
        if re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', i) and re.search(r'<p class="author">'+user+'</p>', i):
            found += 1
            DeletedID = re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', i).group(1)
            cardSyntaxList.remove(i)

    if found == 0:
        logging.error("This article does not exist in this user page. Check the article name or user.")
        sys.exit()
  
    for i in markdownSyntaxList:
        if re.search(r'<zero-md src=".*" id="(\d*)" style="display: none;"></zero-md>', i).group(1) == DeletedID:
            markdownSyntaxList.remove(i)

    
    return [markdownSyntaxList, cardSyntaxList, otherSyntaxList]

def ReorganizeID(syntaxList):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    for i in range(len(markdownSyntaxList)):
        if i != len(markdownSyntaxList) - 1:
            id1 = int(re.search(r'<zero-md src=".*" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i]).group(1))
            id2 = int(re.search(r'<zero-md src=".*" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i+1]).group(1))
            if id1 != id2 + 1:
                markdownSyntaxList[i] = markdownSyntaxList[i].replace(str(id1), str(id2 + 1))
            
    for i in range(len(cardSyntaxList)):
        if i != len(cardSyntaxList) - 1:
            id1 = int(re.search(r'<h3 id="[@|$](\d*)">.*</h3>', cardSyntaxList[i]).group(1))
            id2 = int(re.search(r'<h3 id="[@|$](\d*)">.*</h3>', cardSyntaxList[i+1]).group(1))
            if id1 != id2 + 1:
                cardSyntaxList[i] = cardSyntaxList[i].replace(str(id1), str(id2 + 1))
    
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

def main(articleName, user):
    ## 1. User folder
    html = "../{}/{}".format(user, user) + '.html'
    outputPath = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    CheckExistence(syntaxList, user)
    syntaxList = DeletePosts(syntaxList, articleName, user)
    syntaxList = ReorganizeID(syntaxList)
    WriteSyntaxToHtml(syntaxList, outputPath)

    ## 2. Recent Posts
    html = '../index.html'
    outputPath = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    syntaxList = DeletePosts(syntaxList, articleName, user)
    syntaxList = ReorganizeID(syntaxList)
    WriteSyntaxToHtml(syntaxList, outputPath)

if __name__ == "__main__":
    articleName = "Test modification1"
    user = "JaneDiary"

    main(articleName, user)