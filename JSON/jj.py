import json

nums=[1,2,3,4,5]

filename='nums.json'


"""这样不会报错么？？？"""

with open(filename,'w') as f:
    json.dump(nums,f)