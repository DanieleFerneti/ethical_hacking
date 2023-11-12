import re

line = "This is a sample sentence 0123 !"
matchObj = re.match(r"(.*) sample .* (\d*) .*", line, re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("Nothing found!!")