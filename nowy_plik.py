x = ['a', 'ab', 'abc', 'abcd']

print(x, type(x))

for e in x:
    if 'b' in e:
        print(e)

min = min(x)
print(min)

max = max(x)
print(len(max))

print(x[1])
print()

def efekt(x):
    najkrotsza = x[0]
    for e in x:
        if len(e) < len(najkrotsza):
            najkrotsza = e
    return najkrotsza 

najkrotsza = efekt(x)
print(najkrotsza)
print(len(najkrotsza))

