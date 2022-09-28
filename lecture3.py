'''
ls=[["Tom","Surya","Jenny"],["Mehak","Mami","Badal"]]
for i in ls:
    print(i[0]*2)

print(ls[1][2][::-1])

s=[1,2,3,4,5,6]

s1=set([2,7,4,6])

for i in s1:
    print(i)
'''
#sets are unorders and contain ONLY UNIQUE elements

diction={1:'A',2:'B',3:'C'}
print(diction)
l=[]
for i in diction:
    print(i)
    l.append(i)
    print(diction[i])

#removing spaces without strip

sen = "  i love coffee  "
l = []
for i in sen:
    if i != ' ':
        l.append(i)
print(''.join(l))

#reversing dictionary 

ke = []
va = []
diction2 = {}
for i in diction:
    ke.append(i)
    va.append(diction[i])
for x in ke:
    for y in va:
        diction2[y] = x
print(diction2)
        
    
    
        
