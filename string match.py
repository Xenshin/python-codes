def string_match(s1,s2):
    A = []
    B = []
    if len(s1) == len(s2):
        for i in range(len(s1)):
            for j in range(1,len(s1)):
                if s1[i] == s1[j]:
                    A.append(j) 

        for i in range(len(s2)):
            for j in range(1,len(s2)):
                if s2[i] == s2[j]:
                    B.append(j) 

    if (A == B):
        print('string matched')
    else:
        print('string did not match')

string_match('aba', 'xyz')

# QUESTIONS FROM EDUCATIVE EXAM

A = 46
B = 18
print(A  % B // A)

a=5
b=10
a=a^b
b=a^b
a=a^b
print(a,b)

print(bool())
print(bool('True'))

if (1 < 0) and (0 < -1):
  print("Pass")
elif (1 > 0) or False:
  print("Fail")
else:
  print("Educative")

def factorial(n): 
  return(n*factorial(n-1))  
  factorial(5)

i = 1
while True:
  if i % 5 == 0:
    break
  print(i)
  i += 1

my_string = 'Hello'
for i in range(len(my_string)):
  print (my_string)
  my_string = 'a'


  