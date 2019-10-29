a=[1,4,5,3]

"""powerset of list a
default...1,2,3,4,5...12345...empty

12,13,14,15,23,24,25,34,35,45,

123,124,125,134,135,145,234,235,
245,345,
1234,1235,1245,1345,2345
"""
def powerset(a):

    for i in range(0,len(a)):
        for j in a[i:]:
            k=str(a[:i])+str(j)
            print(k)
    if(len(a)==1):
        print("done")
        return 0
    else:
        powerset(a[1:])
powerset(a)
