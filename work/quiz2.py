def fun(x, y, z = "default value", w = ""):
    return x,y,z

q = fun(1,2,w = "string1")

print(q)