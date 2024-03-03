some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'm']
print(f'this is our list {some_list}')

dupi = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in dupi:
            dupi.append(item)

print(f'this is duplicates in my list {dupi}')
