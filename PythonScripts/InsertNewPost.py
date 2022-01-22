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

def InsertNewPost(syntaxList, md, img, articleName, user, hashTag, abstract):
    markdownSyntaxList = syntaxList[0]
    cardSyntaxList = syntaxList[1]
    otherSyntaxList = syntaxList[2]
    
    for i in cardSyntaxList:
        if re.search(r'<h3 id="(\$)(\d*)">'+articleName+'</h3>', i):
            logging.error("This article already exists! Please change the article name!")
            sys.exit()
    
    markdownSyntax = 5*'\t' + '<zero-md src="{}" id="{}" style="display: none;"></zero-md>'.format(md, len(markdownSyntaxList)+1) + "\n"
    
    if re.match(r'./', md):
        cardSyntax = 5*"\t" + "<div class=\"card\">" + "\n" + 6*"\t" + "<img src=\"{}\">".format(img) + "\n" + 6*"\t" + "<div class=\"abstract\">" + "\n" + 7*"\t" + "<h3 id=\"@{}\">{}</h3>".format(len(cardSyntaxList)+1, articleName) + "\n" + 7*"\t" + "<p class=\"author\">{}</p>".format(user) + "\n" + 7*"\t" + "<p class=\"hashTag\">{}</p>".format(hashTag) + "\n" + 7*"\t" + "<p class=\"abstractContent\">{}</p>".format(abstract) + "\n" + 6*"\t" + "</div>" + "\n" + 5*"\t" + "</div>" + "\n" + "\n"
    else:
        cardSyntax = 5*"\t" + "<div class=\"card\">" + "\n" + 6*"\t" + "<img src=\"{}\">".format(img) + "\n" + 6*"\t" + "<div class=\"abstract\">" + "\n" + 7*"\t" + "<h3 id=\"${}\">{}</h3>".format(len(cardSyntaxList)+1, articleName) + "\n" + 7*"\t" + "<p class=\"author\">{}</p>".format(user) + "\n" + 7*"\t" + "<p class=\"hashTag\">{}</p>".format(hashTag) + "\n" + 7*"\t" + "<p class=\"abstractContent\">{}</p>".format(abstract) + "\n" + 6*"\t" + "</div>" + "\n" + 5*"\t" + "</div>" + "\n" + "\n"
    
    markdownSyntaxList.insert(0, markdownSyntax)
    cardSyntaxList.insert(0, cardSyntax)
    
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

def main(md, img, articleName, user, hashTag, abstract):
    ## 1. User folder
    html = "../{}/{}".format(user, user) + '.html'
    output = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html)
    syntaxList = InsertNewPost(syntaxList, md, img, articleName, user, hashTag, abstract)
    WriteSyntaxToHtml(syntaxList, output)

    ## 2. Recent Posts
    md = "./{}/{}".format(user, md)
    html = '../index.html'
    output = '{}/New.html'.format(os.path.dirname(html))
    syntaxList = ExtractMarkdownAndCardSyntaxToList(html) 
    syntaxList = InsertNewPost(syntaxList, md, img, articleName, user, hashTag, abstract)
    WriteSyntaxToHtml(syntaxList, output)
    
if __name__ == "__main__":
    md = "Handbook_css.md"
    img = "./shortCut/rs6250_thinkstockphotos-495070930-low.jpeg"
    articleName = "Handbook of computational social science"
    user = "JaneNote"
    hashTag = "#Computational social science #Digital trace"
    abstract = "DIGITAL TRACE DATA: Modes of data collection, applications, and errors at a glance"
    
    main(md, img, articleName, user, hashTag, abstract)