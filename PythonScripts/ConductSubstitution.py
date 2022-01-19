##Conduct the substitution.
import os
import logging
import sys
logging.basicConfig(level=logging.NOTSET)

def ConductSubstitution(html, newHtml):
    if os.path.exists(html) and os.path.exists(newHtml):
        os.rename(html, html.replace(".html","_backup.html"))
        os.rename(newHtml, html)
    else:
        logging.error("The html file {} or {} does not exist".format(html, newHtml))
        sys.exit()
        
if __name__ == "__main__":
    user = "LeoNote"
    
    recentPost = "../index.html"
    newRecentPost = "../New.html"
    userFolder = "../{}/{}.html".format(user, user)
    newUserFolder = "../{}/New.html".format(user)
    
    ConductSubstitution(userFolder, newUserFolder)
    ConductSubstitution(recentPost, newRecentPost)
    
    