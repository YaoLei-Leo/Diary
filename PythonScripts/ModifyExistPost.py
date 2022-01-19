##To insert new post to the specific part and recent posts
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

def ModifyExistPost(syntaxList, articleName, user, md, img, hashTag, abstract):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    for i in range(len(cardSyntaxList)):
        if re.search(r'<h3 id="[@|$](\d*)">'+articleName+'</h3>', cardSyntaxList[i]) and re.search(r'<p class="author">(.*)</p>', cardSyntaxList[i]).group(1) == user:
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
                for i in range(len(markdownSyntaxList)):
                    if re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i]).group(2) == ID:
                        originalMd = re.search(r'<zero-md src="(.*)" id="(\d*)" style="display: none;"></zero-md>', markdownSyntaxList[i]).group(1)
                        if md != originalMd:
                            cardSyntaxList[i] = markdownSyntaxList[i].replace(originalMd, md)
                            logging.info("Markdown src was changed") 

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
    articleName = "Venn Plot using R"
    user = "LeoNote"
    
    md = "VennPlot.md"
    img = "123TripleVennPlot.png"
    hashTag = "#123"
    abstract = "123Powerpoint default venn plot method does not offer proportional venn circles. Therefore, I use R package eulerr to acheive this aim."
    
    main(articleName, user, md, img, hashTag, abstract)