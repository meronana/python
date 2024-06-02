#JSON files - data format
#App to app communications

"""
{
    name: Bryan
    age: 46
    pet: Cat
}
"""

#Imports
import json
fielname = 'json.txt'

#dict to json
outD = dict(name = 'Bryan', age =46, pet = 'Cat')
s = json.dumps(outD) #dump out String
print(f'String = {s}')

#push it out to file
with open(fielname,'w') as f:
    json.dump(outD,f) #Dump puts it to file

#From String
inD = json.loads(s) # Load the dictionary from the string
print(f'Dictionary = {inD}')

#From file
with open(fielname, 'r') as f:
    p = json.load(f)
print(f'Type: {type(p)} = {p}') #print what data type it is


