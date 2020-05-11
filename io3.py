import json

data = {'id':11,'name':'raj'}

with open('myfile.txt','w+') as f:
    json.dump(data,f)

'''
x = json.dumps(data)
print(x)
with open('myfile.txt','w+') as f:
    f.write(x)
'''

