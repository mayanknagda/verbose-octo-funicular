def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

def new(a,b):
	j=min(a)
	k=min(b)
	l1=min(j,k)
	z= a.index(j);
	y= b.index(k);
	s1=second_smallest(a)
	s2=second_smallest(b)
	if(z==y):
		m1= min(s1,s2)
		print(m1+l1)

	else:
		print(j+k)

x = int(input().strip())
a1 = list(map(int, input().strip().split(' ')))
b2 = list(map(int, input().strip().split(' ')))
new(a1,b2);
