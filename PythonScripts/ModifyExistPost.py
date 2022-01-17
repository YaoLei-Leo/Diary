##To modify an specific posts in both the recent post and user's folder.
import re
import sys
import os

def DetectInsertionPos(html):
    with open(html) as f:
        MdInsertPos = 0; CardInsertPos = 0;
        for line1 in f:
            if re.search("<!-- Markdown insert position -->", line1):
                print("DetectInsertionPos: Markdown insertion position detected")
                MdInsertPos += 1
            if re.search("<!-- Card insert position -->", line1):
                print("DetectInsertionPos: Card insertion position detected")
                CardInsertPos += 1
        if MdInsertPos ==1 and CardInsertPos==1:
            return 0
        elif MdInsertPos ==0 or CardInsertPos==0:
            print("DetectInsertionPos: Error: MdInsertPos not detected or CardInsertPos not detected!")
            sys.exit()
        else:
            print("DetectInsertionPos: Error: More than 1 MdInsertPos or CardInsertPos are detected!")
            sys.exit()

def DetectIDIntegrity(html, prefix):
    with open(html) as f:
        Integrity = 0
        for line1 in f:
            if re.search("<!-- Markdown insert position -->", line1):
                line1 = f.readline()
                id = re.search(r'id=\"(\d*)\"', line1).group(1)
                print("DetectIDIntegrity: There are {} articles exist.".format(id))
                
            if re.search("<!-- Card insert position -->", line1):
                for line2 in f:
                    if re.search(r'id=\"(.\d*)\"', line2):
                        CardId = re.search(r'id=\"(.\d*)\"', line2).group(1)
                        if CardId.replace(prefix,"") == id:
                            print("DetectIDIntegrity: The CardID is same as MdID")
                            Integrity = 1
                            break
        if Integrity == 1:
            print("DetectIDIntegrity: Document integrity is OK.")
            return 0
        else:
            print("DetectIDIntegrity: Error: Document is not OK.")
            sys.exit()

# def ModifyExistPost(html):

if __name__ == "__main__": 
    md = "test.md"
    img = ""
    articleName = ""
    user = "Jane"
    hashTag = ""
    abstract = "Modification test"
    
    # 1. Test file integrity
    ## 1.1 Recent Posts
    html = "../InsertTest.html"
    if DetectInsertionPos(html) == DetectIDIntegrity(html, "@") == 0:
        print("ModiftyExistPost: Main: {} Document are correct".format(html))
    else:
        print("Main: {} Document are not correct".format(html))
        sys.exit()
    ## 1.2 User folder
    if user == "Puppy":
            html = "../PuppyDiary/Puppy.html"
    elif user == "Xuxu":
        html = "../XuxuDiary/Xuxu.html"
    elif user == "Leo":
        html = "../LeoNote/LeoNote.html"
    elif user == "Jane":
        html = "../JaneNote/InsertTest.html"
        
    if DetectInsertionPos(html) == DetectIDIntegrity(html, "$") == 0:
        print("ModiftyExistPost: Main: {} Document are correct".format(html))
    else:
        print("Main: {} Document are not correct".format(html))
        sys.exit()

    # 1. Test file integrity