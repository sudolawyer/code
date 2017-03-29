```Python
# This script will scan a plain text document looking for legal citations in the document.
# It will then print all of the unique citations, line by line, as well as the total number
# of unique citations used to craft the opinion.  In this example I use Chevron, which cites 
# 50 unique cases throughout the opinion.


#Created by: Stephan S. Dalal
#Affiliation: Georgetown Law
#Language: Python3
#Date: March 2017

import re
import requests

opinionString = open("chevron.txt", encoding="utf-8", errors="ignore").read()

def opinionCitation(opinionString):
    
    citationRegex = '\d{1,3} U.S. \d{1,4}'
    match = re.findall(citationRegex, opinionString)
    uniqueMatches = len(match)
    citationElement=True
    citationReplace=True
    
    i = 0
    j = -1
    while i < int(uniqueMatches):
        
        citationElement=match[i]
        citationReplace = citationElement.replace(" ", "+")
        baseURL = "https://www.courtlistener.com/?type=o&q="
        endURL="&type=o&order_by=score+desc&start_Precedential=on"
        URL=True
        
        while j <= i:
            
            URL = (baseURL + citationReplace + endURL)
            print(URL)
            j+=1


        #print("Citation ELEMENT FOR i: ", i, "is ", citationElement)
        i +=1
