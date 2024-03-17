# Regex module
# match() function checks for a match only at the beginning of the string
# group() is a method used to retrieve the portion of the string that matched the regular expression pattern
#\w return each character seqentially

# import re
# string="K Sai kiran"
# m=re.match('K',string)
# print(m)       #<re.Match object; span=(0, 1), match='K'>


# import re
# string="K Sai kiran"
# m=re.match('K',string)
# m1=m.group()
# print(m1) 

# import re
# pattern=r'(\w+\s\w+)'
# string="Sai kiran"
# m=re.match(pattern,string)
# m1=m.group()
# print(m1)           #Sai kiran



# import re

# string = "Saikumar@gmail.com"
# pattern = r'(\w+)@(\w+).(\w+)'

# w=re.search(pattern,string)

# print(w.group(0))
# print(w.group(1))
# print(w.group(2))
# print(w.group(3))
# print(w.group(1,2,3))

#task: groupdict()
# import re
# string = "Saikumar@gmail.com"
# pattern = r'(?P<username>\w+)@(?P<gmail>\w+).(?P<com>\w+)'
# w=re.match(pattern,string)
# print(w.groupdict())            #{'username': 'Saikumar', 'gmail': 'gmail', 'com': 'com'}

import re
pattern=r"programming.*"
string="The python programming is very easy to learn"
w=re.search(pattern,string)
print(w.group())                      #programming is very easy to learn



