import re

#sequence of characters that defines a search module
'''
1. [] => "[a-p]"
2. \d => all digits
3. . => #anything with he and any three character ...
4. ^ => starting
5. $ => ending
6. * => zero or more times
7. + => one or more times
8. {} => exact string => "hell{o}"
9. | => exact match of first or second key
10. [0-9]
'''

pattern = '^a...s$'
tstring1 = 'abbbbbyyyyyyysssss bbb abb aabb aaa'
tstring2 = 'helllo worllld rhelllo world hells hellss hell '
tstring3 = 'The India and Spain are in 21st century and India Ind'
result1 = re.match(pattern,tstring1)
result2 = re.match(pattern,tstring2)
result3 = re.search("^The.*India$",tstring3)
result4 = re.findall("[a-d]",tstring3) #from a to d
result5 = re.findall("\d",tstring3) #all digits
result6 = re.findall("he...",tstring2) #anything with he and any three character ...
result7 = re.findall("^India",tstring3) #starting with India but its there
result8 = re.findall("^The",tstring3) #starting with The
result9 = re.findall("century$",tstring3)
result10 = re.findall("hello*",tstring2)
result11 = re.findall("he*",tstring2)
result12 = re.findall("ab*",tstring1) #a then zero or more times b any possiblity
result13 = re.findall("ab+",tstring1) #a then one or more times b any possiblity
result14 = re.findall('rl{3}',tstring2) #exact times of occurance of l rl{3}
result15 = re.findall('India|Spain',tstring3) #exact match of first or second key
result16 = re.search('India|Spain',tstring3) #first match object
result17 = re.split('India|Spain',tstring3) #split result after match
result18 = re.sub('India|Spain','China',tstring3) #substitute
result19 = re.sub('India|Spain','China',tstring3,2) #substitute only 2 matches
'''
findall => returns list of matches
search => returns match object of first success match
split => list of split leftovers test string
sub => substitute success matches
'''

print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result11)
print(result12)
print(result13)
print(result14)
print(result15)
print(result16.start())
print(result17)
print(result18)
print(result19)
#print(result1)
#print(result2)
#print(result3)

'''
if result2:
    print("successful")
else:
    print("unsuccessful")
'''