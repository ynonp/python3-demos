s = set([10, 20])


s.add(30)
s.add(30)
s.add(30)
s.add(30)
s.add(30)

s.add('foo')

print(s)

if 10 in s:
    print('10 is in the set')

# for item in s:
#     print(item)
    
print(len(s))