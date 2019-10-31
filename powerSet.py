a=[1,4,5,3]

"""powerset of list a
default...1,2,3,4,5...12345...empty

12,13,14,15,23,24,25,34,35,45,

123,124,125,134,135,145,234,235,
245,345,
1234,1235,1245,1345,2345
"""
def powerSet(lst, res=[], step=1): 
	'''works for sets of max 4 elements'''
	if len(lst) < 2:
		res.append(lst)
		res.append([])
		return res
	for i in range(len(lst)):
		for j in range(len(lst)):
			if step == 1 :
				subset = lst[i: j+1: step]
			else:
				subset = lst[i: j: step-1] + lst[j::step]
			if res.count(subset) == 0:
				res.append(subset)
	if step <= len(res):
		return powerSet(lst, res, step+1)
	res.sort()
	return res, len(res)
print(powerSet(a))
