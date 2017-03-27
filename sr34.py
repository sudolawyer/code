```python
import sys
import re
import os

print(os.getcwd())
text = open("sres34.txt").read()
#print(text)

alltext = re.findall("[A-Z]-",text)
allTextTotal = len(alltext)
print("TOTAL SENATORS IN THE VOTE: ", len(alltext))

republicans = re.findall("R-",text)
print("REPUBLICANS: ", len(republicans))

democrats = re.findall("D-", text)
print("DEMOCRATS: ", len(democrats))

others = re.findall("I-",text)
print("INDEPENDENTS: ", len(others))

total = len(democrats) + len(republicans) + len(others)
print("TOTAL: ", total)

if total == allTextTotal:
    print ("CORRECT: TOTAL MATCHES")
else:
    print("ERROR: TOTALS DO NOT MATCH")

textRows = text.split('\n')

for each in textRows:
    new = each.split('(')
    print(new)
    



```
