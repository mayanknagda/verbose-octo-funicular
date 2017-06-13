import sys

def patternCount(s):
	l=len(s)
	su=0
	for i in range(l):
		if s[i]=='1':
			j=i+1;
			if j<l-1:
				if s[j]=='1':
					continue
			su=su+1
			for j in range(j,l):
				if s[j]=='0':
					continue;
				if s[j]=='1':
					break
				else:
					su=su-1
					break;
		else:
			continue
	if s[l-1]=='0':
		su=su-1
	elif s[l-1] =='1':
		su=su-1
	if s[l-1] == '1' and s[l-2] == '1':
		su=su-1
	if su<0:
		su=0;
	
	return su
			


    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
