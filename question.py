def getkey(obj:dict):
  keys = list(obj)
  if len(keys)!=1;
      raise Exception('multiple keys / empty dict')
  else:
     return keys[0]

def getNestedValue(obj:dict, key:str, isFound = False):

 if type(obj) is not dict and notisFound:
    return None
 if (isFound or (key in obj.keys())):
     if type(obj[key]) is dict:
        return getNestedValue(obj[key], getKey(obj[key]),
True)
    else:
       return obj[getKey(obj)]
 else:
    nestedKey = getKey(obj)
    return getNestedValue(obj[nestedKey], key,False)

if_name_=='_main_':
   obj = {'a':{'b':{'c':'d'}}}
   value = getNestedValue(obj,'a')
    print(value) 
 