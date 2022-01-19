##To insert new post to the specific part and recent posts
import re
import sys
import os
import logging
logging.basicConfig(level=logging.NOTSET)

def DetectInsertionPos(html):
    with open(html) as f:
        MdInsertPos = 0; CardInsertPos = 0;
        for line1 in f:
            if re.search("<!-- Markdown insert position -->", line1):
                logging.info("Markdown insertion position detected")
                MdInsertPos += 1
            if re.search("<!-- Card insert position -->", line1):
                logging.info("Card insertion position detected")
                CardInsertPos += 1
        if MdInsertPos ==1 and CardInsertPos==1:
            return 0
        elif MdInsertPos ==0 or CardInsertPos==0:
            logging.error("MdInsertPos not detected or CardInsertPos not detected!")
            sys.exit()
        else:
            logging.error("More than 1 MdInsertPos or CardInsertPos are detected!")
            sys.exit()
            
def DetectIDIntegrity(html, prefix):
    with open(html) as f:
        Integrity = 0
        for line1 in f:
            if re.search("<!-- Markdown insert position -->", line1):
                line1 = f.readline()
                id = re.search(r'id=\"(\d*)\"', line1).group(1)
                logging.info("There are {} articles exist.".format(id))
                
            if re.search("<!-- Card insert position -->", line1):
                for line2 in f:
                    if re.search(r'id=\"(.\d*)\"', line2):
                        CardId = re.search(r'id=\"(.\d*)\"', line2).group(1)
                        if CardId.replace(prefix,"") == id:
                            logging.info("The CardID is same as MdID")
                            Integrity = 1
                            break
        if Integrity == 1:
            logging.info("DetectIDIntegrity: Document integrity is OK.")
            return 0
        else:
            logging.error("DetectIDIntegrity: Error: Document is not OK.")
            sys.exit()


def InsertToHtml(pos, html, md, img, articleName, user, hashTag, abstract):
    # Get the number of posts exists
    with open(html) as f:
        for line1 in f:
            if re.search("<!-- Markdown insert position -->", line1):
                line1 = f.readline()
                id = re.search(r'id=\"(\d*)\"', line1).group(1)
    # Create new output file.
    output = open("{}/New.html".format(os.path.dirname(html)), 'w')
    with open(html) as f:
        newId = int(id) + 1
        for line1 in f:
            # Insert markdown syntax
            if re.search("<!-- Markdown insert position -->", line1):
                if user == "PuppyDiary" or user == "XuxuDiary" or user == "LeoNote" or user == "JaneNote":
                    if pos == "@": # For recent posts
                        line1 = line1 + 5*'\t' + "<zero-md src=\"./{}/{}\" id=\"{}\" style=\"display: none;\"></zero-md>".format(user, md, newId) + "\n"
                    elif pos == "$": # For user folder
                        line1 = line1 + 5*'\t' + "<zero-md src=\"{}\" id=\"{}\" style=\"display: none;\"></zero-md>".format(md, newId) + "\n"
                    else:
                        logging.error("Input pos is tag is not right.")
                        sys.exit()
                else:
                    logging.error("User not exists")
                    sys.exit()
            
            if re.search("<!-- Card insert position -->", line1):
                    line1 = line1 + 5*"\t" + "<div class=\"card\">" + "\n"
                    if pos == "@": # For recent posts
                        line1 = line1 + 6*"\t" + "<img src={}/{}>".format(user,img) + "\n"
                    else: # For user folder
                        line1 = line1 + 6*"\t" + "<img src={}>".format(img) + "\n"
                    line1 = line1 + 6*"\t" + "<div class=\"abstract\">" + "\n"
                    if pos == "@": # For recent posts
                        line1 = line1 + 7*"\t" + "<h3 id=\"@{}\">{}</h3>".format(newId, articleName) + "\n"
                    else: # For user folder
                        line1 = line1 + 7*"\t" + "<h3 id=\"${}\">{}</h3>".format(newId, articleName) + "\n"
                    line1 = line1 + 7*"\t" + "<p class=\"author\">{}</p>".format(user) + "\n"
                    line1 = line1 + 7*"\t" + "<p class=\"hashTag\">{}</p>".format(hashTag) + "\n"
                    line1 = line1 + 7*"\t" + "<p class=\"abstractContent\">{}</p>".format(abstract) + "\n"
                    line1 = line1 + 6*"\t" + "</div>" + "\n" + 5*"\t" + "</div>" + "\n" + "\n"
            output.write(line1)

def ConductSubstitution(html, newhtml):
    if os.path.exists(html):
        os.remove(html)
        os.rename(newhtml, html)
    else:
        print("The {} file does not exist".format(html))
        
def main(md, img, articleName, user, hashTag, abstract):
    # 1. Test file integrity
    ## 1.1 Recent Posts
    html = "../index.html"
    if DetectInsertionPos(html) == DetectIDIntegrity(html,"@") == 0:
        logging.info("Main: {} Document are correct".format(html))
    else:
        logging.error("Main: Error: {} Document are not correct".format(html))
        sys.exit()

    ## 1.2 User folder.
    if user == "PuppyDiary" or user == "XuxuDiary" or user == "LeoNote" or  user == "JaneNote":
        html = "../{}/{}.html".format(user, user)
        if DetectInsertionPos(html) == DetectIDIntegrity(html,"$") == 0:
            logging.info("Main: {} Document are correct".format(html))
        else:
            logging.error("Main: {} Document are not correct".format(html))
            sys.exit()
    else:
        logging.error("Main: Error: {} user not exists".format(user))
        sys.exit()
    
    # 2. Begin insertion
    ## 2.1 Recent Posts
    html = "../index.html"
    # InsertToRecentPosts(html, md, img, articleName, user, hashTag, abstract)
    InsertToHtml("@", html, md, img, articleName, user, hashTag, abstract)
    # ConductSubstitution(html, "../New.html")
    ## 2.2 User folder.
    if user == "PuppyDiary" or user == "XuxuDiary" or user == "LeoNote" or  user == "JaneNote":
        html = "../{}/{}.html".format(user,user)
    # InsertToUserFolder(html, md, img, articleName, user, hashTag, abstract)
    InsertToHtml("$", html, md, img, articleName, user, hashTag, abstract)
    
    # 3. Conduct substitution
    ## 3.1 Recent Posts
    html = "../index.html"
    ConductSubstitution(html, "{}/New.html".format(os.path.dirname(html)))
    ## 3.2 User folder.
    if user == "PuppyDiary" or user == "XuxuDiary" or user == "LeoNote" or  user == "JaneNote":
        html = "../{}/{}.html".format(user,user)
    ConductSubstitution(html, "{}/New.html".format(os.path.dirname(html)))

if __name__ == "__main__":
    md = "AiDigitalMedia.md"
    img = "https://righttoinformation.wiki/_media/explanations/rti-information.jpg"
    articleName = "Computational Communication Science"
    user = "JaneNote"
    hashTag = "#Method #Communication"
    abstract = ""
    
    img = md.replace(".md","_src/") + img
    
    main(md, img, articleName, user, hashTag, abstract)