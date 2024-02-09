d = {'foo': 1, 'bar': 2, 'baz': 3}
while d:
    print(d.popitem())
print('Done')


d1 = {'foo': 1, 'bar': 2, 'baz': 3}
print(len(d1))

d1 = {'foo': 1, 'bar': 2, 'baz': 3}
while len(d1) > 3:
    print(d1.popitem())
print('Done')

a = [1,2,3,4,5]
print(len(a))
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done')


