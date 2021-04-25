
def nested_dict(dictionary, k):
    for key, val in dictionary.items():
        if key == k:
            return val
        if isinstance(val, dict):
            nested_res = nested_dict(val, k)
            if nested_res:
                return nested_res
    return None


object1 = {'a':{'b':{'c':'d'}}}
object2 = {'x':{'y':{'z':'a'}}}
print(nested_dict(object2, 'z'))