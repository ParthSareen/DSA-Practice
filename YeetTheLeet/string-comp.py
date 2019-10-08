l = ['a', 'a', 'b', 'c', 'c', 'c']

d = {}


def func(l, d):
	for x in range(len(l)):
		if l[x] in d:
			d[l[x]] += 1

		else:
			d[l[x]] = 1
	return d

def conv(c):
	ans = []
	for key in c:
		ans.append(key)
		ans.append(c[key])
	return ans

print(conv(func(l,d)))