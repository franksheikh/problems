groups = {}

count = [0] * 26
for c in 'abc':
	count[ord(c) - ord('a')]+=1

key = tuple(count)
if key not in groups:
    groups[key] = []

print('groups',groups)
    