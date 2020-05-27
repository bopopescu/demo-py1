mydict1 = {'name':'raj','rollno':101,'sub':'cs'}
mydict2 = {'name':'rajesh','rollno':102,'sub':'ec'}

#result_dict3 = {'name':['raj','rajesh'],'rollno':[101,102],'sub':['cs','ec']}

#mydict1.items(),keys(),values()
'''
for k,v in mydict1.items():
    #print(mydict1)
    print(k)
    print(v)

for i in mydict1.keys():
    print(i)

for i in mydict1.values():
    print(i)
'''

mydict3 = {'a':11,'b':12,'c':13,'d':14}
result_dict = {} #{'a':22,'b':24,'c':26}
result_dict = {} #{'b':24,'d':28}

for k,v in mydict3.items():
    #result_dict.update([(k,v*2)])
    result_dict[k] = v*2

print(result_dict)

# result_dict = {k:v for (k,v) in dict.items()}
#result_dict = {k:v*2 for (k,v) in mydict3.items()}
result_dict = {k:v*2 for (k,v) in mydict3.items() if v%2==0}
print(result_dict)

