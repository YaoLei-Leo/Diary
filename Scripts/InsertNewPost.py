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
    md = "test.md"
    img = "data:image/png;base64,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"
    articleName = "Test"
    user = "JaneDiary"
    hashTag = "#Test"
    abstract = "Test"
    
    main(md, img, articleName, user, hashTag, abstract)