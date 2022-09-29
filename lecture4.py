#Sum of one in two values of a dict
'''
s={"kohli":1,
   "D":2,
   "st":3,
   "Kane":4,
   "J"












   :5}
ls = []
n=0
for i,j in zip(s.keys(),s.values()):
    ls.append(j)
for k in ls[::2]:
    n += k
print(n)
'''
#Add values of a dictionary and their sum into a list(but values of dict must be in reverse direction)
'''
s = {"Kohli" : "kohli",
     "Dhoni" : "dhoni",
     "Kane" : "kane"}
s1 = {"kohli" : 23,
      "dhoni" : 69,
      "kane" : 68,
      "jacob" : 98}
      
ls = []
total = 0
for i,j in zip(s.keys(),s.values()):
    for k,l in zip(s1.keys(),s1.values()):
        if j == k:
            ls.append(l)
ls1 = ls[::-1]
for i in ls1:
    total += i
ls1.append(total)
print(ls1)
'''
#print every second key in s2 that is also a value in s1
'''
s1 = {"kohli" : 23,
      "dhoni" : 69,
      "kane" : 68,
      "jacob" : 98}
s2 = {23:46,
      69:138,
      68:136,
      98:196}
ls = []
for i,j in zip(s1.keys(),s1.values()):
    for k,l in zip(s2.keys(),s2.values()):
        if j == k:
            ls.append(l)
print(ls[::-2])
'''
        
    
    
