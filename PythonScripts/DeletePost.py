##To delete a post in the user folder and recent posts.
import re
import sys
import os
import logging
logging.basicConfig(level=logging.NOTSET)

def ExtractMarkdownAndCardSyntaxToList(html):
    markdownSyntaxList = list()
    cardSyntaxList = list()
    otherSyntaxList = list()
    otherSyntax = ''
    with open(html) as f:
        for line1 in f:
            if re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', line1):
                if otherSyntax != '':
                    otherSyntaxList.append(otherSyntax)
                    otherSyntax = ''
                markdownSyntaxList.append(line1)
                
            elif re.search(r'<div class="card">', line1):
                if otherSyntax != '':
                    otherSyntaxList.append(otherSyntax)
                    otherSyntax = ''
                cardSyntax = line1
                for i in range(1, 10):
                    line2 = f.readline()
                    cardSyntax = cardSyntax + line2
                cardSyntaxList.append(cardSyntax)
            else:
                otherSyntax = otherSyntax + line1
        otherSyntaxList.append(otherSyntax)
    # print(markdownSyntaxList)
    # print(cardSyntaxList[0])
    # print(otherSyntaxList[2])
    return [markdownSyntaxList, cardSyntaxList, otherSyntaxList]

def DeletePosts(syntaxList, articleName, user):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    for i in cardSyntaxList:
        if re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', i) and re.search(r'<p class="author">'+user+'</p>', i):
            DeletedID = re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', i).group(1)
            cardSyntaxList.remove(i)
    
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

if __name__ == "__main__":
    articleName = "Venn Plot using R 1"
    user = "LeoNote"
    
    html="../index.html"
    outputPath="../New.html"
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    syntaxList = DeletePosts(syntaxList, articleName, user)
    syntaxList = ReorganizeID(syntaxList)
    WriteSyntaxToHtml(syntaxList, outputPath)