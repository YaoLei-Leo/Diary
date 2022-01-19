##Conduct the substitution.
import os
import logging
import sys
logging.basicConfig(level=logging.NOTSET)

def ConductSubstitution(html, newHtml):
    if os.path.exists(html) and os.path.exists(newHtml):
        os.remove(html)
        os.rename(newHtml, html)
    else:
        logging.error("The html file {} or {} does not exist".format(html, newHtml))
        sys.exit()
        
if __name__ == "__main__":
    recentPost = "../index.html"
    newRecentPost = "../New.html"
    user = "JaneNote"
    userFolder = "../{}/{}.html".format(user, user)
    newUserFolder = "../{}/New.html".format(user)
    
    ConductSubstitution(userFolder, newUserFolder)
    ConductSubstitution(recentPost, newRecentPost)
    
    