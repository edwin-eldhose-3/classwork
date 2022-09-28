#Q1
'''
ls1 = [1,2,3]
ls2 = [4,5,6]

for i in range(0,3):
    print(ls1[i],ls2[i],end='   ')
'''
#Q2
'''
ls1 = [5,10,15,20,25,50,20]
query = int(input("Enter number to be changed"))
replace = int(input("Enter replacing number"))
x = 0
for i in ls1:
    if query == i:
        ls1[x] = replace
    else:
        x += 1
print(ls1," is the current list")
'''
#Q3
'''
ls1 = [1,2,3]
ls2 = []

for i in ls1[::-1]:
    ls2.append(i)
print(ls2)
'''
#Q4
'''
s1= str(input("Enter a string "))
s2= ''
for i in s1:
    if i == 's':
        s2 += 'c'
    else:
        s2 += i
print(s2)
'''
#Q5
'''
s1 = str(input("Enter a string "))
s2 = ''
for i in s1[::-1]:
    s2 += i
print(s2[::-1])
'''
#Q6
'''
s1 = 'My name is Sahib'
s2 = ''
for i in s1:
    if i != ' ':
        s2 += i
print(s2)
'''
        

        
        
