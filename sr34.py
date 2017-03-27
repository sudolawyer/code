```python
# Created by Stephan S. Dalal
# 3-27-2017
# For: Python 3
# Affiliation: Georgetown Univetrsity Law; Washington, DC

import sys
import re
import os

print(os.getcwd()) # prints working directory 
text = open("sres34.txt").read() # opens our text file so we know who voted for what
#print(text)

# Let's do a quick count of the total votes SR 34 received
alltext = re.findall("[A-Z]-",text)
allTextTotal = len(alltext)
print("TOTAL SENATORS IN THE VOTE: ", len(alltext))

# Now let's split the count of votes by party
republicans = re.findall("R-",text)
print("REPUBLICANS: ", len(republicans))

democrats = re.findall("D-", text)
print("DEMOCRATS: ", len(democrats))

others = re.findall("I-",text)
print("INDEPENDENTS: ", len(others))

# Let's do some verification to make sure we didn't miss any votes
total = len(democrats) + len(republicans) + len(others)
print("TOTAL: ", total)

if total == allTextTotal:
    print ("CORRECT: TOTAL MATCHES")
else:
    print("ERROR: TOTALS DO NOT MATCH")

# Now let's clean the data up so we can do something cool with it 
# I want to isolate SENATOR, PARTY, STATE, VOTE and store that data as csv
textRows = text.split('\n') 

for each in textRows:
    new = each.split('(')
    print(new)
    



```
