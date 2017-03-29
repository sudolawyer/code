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

opinionString = open("chevron.txt", encoding="utf-8", errors="ignore").read() #some unicode error magic

def opinionCitation(opinionString):

    citationRegex = '\d{1,3} U.S. \d{1,3}'
    match = re.findall(citationRegex, opinionString)
    print(match)
    uniqueMatches=len(match)
    for each in match:
        matches = each.split('\n')
        print(matches)
    print("TOTAL UNIQUE CITATIONS: ", uniqueMatches)
    
opinionCitation(opinionString)
```
