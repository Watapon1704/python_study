def key_func(n):
    return int(n)
 
 
l = [2, 3, 4, '111']
 
print(min(l, key=key_func))
print(max(l, key=key_func))