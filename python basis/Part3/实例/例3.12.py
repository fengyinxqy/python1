dict2 = {'Jerry': 8, 'Tom': 10, 'Lily': 9}
print(len(dict2))
print(type(dict2))
print(str(dict2))
print(dict2.items())
print(dict2.keys())
print(dict2.values())
print(dict2.get('Lily', 20))
print(dict2.get('Luck', 18))
print(dict2.pop('Lily', 20))
print(dict2.popitem())
print(dict2)
dict3 = dict2.fromkeys('ABCDEF', 9)
print(dict3)
print(dict2)
dict3.update(dict2)
print(dict3)
dict2.setdefault('Jerry', 16)
print(dict2)
dict2.setdefault('Lily', 10)
print(dict2)
