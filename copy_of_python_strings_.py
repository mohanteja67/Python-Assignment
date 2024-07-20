# -*- coding: utf-8 -*-
"""Copy of Python Strings .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ZSfSbgqBx2qaGf9_0vLfQ1zjM_bS8vq

### Question 1: Write a Python program to count the number of characters in a string without using len function.

- `sample input : `
    - `var = 'python java'`
- `sample output :`
    - `result : 11`
"""

# Please write The solution Here for above question 1:
var=input("Enter any Character : ")
c=0
for i in var:
  c=c+1
print(c)

"""### Question 2: Write a Python program to reverse a string without using [::-1]

- `sample input : `
    - `var = 'python'`
- `sample output :`
    - `result : nohtyp`
"""

# Please write The solution Here for above question 2:
var = input("Enter any Character : ")
reverse=""
for i in range(len(var)-1,-1,-1):
  reverse+=var[i]
print(reverse)

"""### Question 3: Write a Python program to check if a string is a palindrome don't use [::-1].

- `sample input : `
    - `var = 'NUN'`
- `sample output :`
    - `result : It is a Palindrome`
    
- `palindrome concept = https://www.dictionary.com/e/palindromic-word/#:~:text=A%20palindrome%20is%20a%20word,roots%20in%20the%20early%201600s.`
"""

# Please write The solution Here for above question 3:
var=input("Enter any Character : ")
reverse=(var[::-1])
if reverse==var:
  print(f"The Character {var} Palindrome")
else:
  print(f"The Character {var} not a Palindrome")

"""### Question 4: Write a Python program to find the most common character in a string.

- `sample input : `
    - `var = 'Hello world '`
- `sample output :`
    - `result : l, because l is repeating 3 times `
"""

# Please write The solution Here for above question 4:
var=input("Enter any Character : ")
dict1={}
for char in var:
  if char in dict1:
    dict1[char]+=1
  else:
    dict1[char]=1
    common=max(dict1,key=dict1.get)
print(common,dict1[common])

"""### Question 5: Write a Python program to check if two strings are anagrams.

- `sample input : `
    - `var1 = 'listen'`
    - `var2 = 'silent'`
- `sample output :`
    - `result : both are anagram because characters in var2 is in var1`
"""

# Please write The solution Here for above question 5:
var1=input("Enter any Character : ")
var2=input("Enter any Character : ")
if len(var1) !=len(var2):
  print(False)
sorted_var1=sorted(var1)
sorted_var2=sorted(var2)
print(sorted_var1==sorted_var2)

"""### Question 6: Write a Python program to remove all the vowels from a string.

- `sample input : `
    - `var = 'python'`
- `sample output :`
    - `result : pythn , because vowels are [AEIOUaeiou]`
"""

# Please write The solution Here for above question 6:
var=input("Enter any Character : ")
vowels="aeiouAEIOU"
result=[]

for char in var:
  if char not in vowels:
    result.append(char)
    var.join(result)
print(result)

"""### Question 7: Write a Python program to find the longest word in a string.

- `sample input : `
    - `var = 'python is Easy Language'`
- `sample output :`
    - `result : Language`
"""

# Please write The solution Here for above question 7:
var=input("Enter any Character : ")
words=var.split()
longest=""
length=0
for word in words:
  if len(word)>length:
    longest=word
    length=len(word)
print(longest)

"""### Question 8: Write a Python program to capitalize the first letter of each word in a string [dont use built-in-function title].

- `sample input : `
    - `var = 'python is easy'`
- `sample output :`
    - `result : Python Is Easy`
"""

# Please write The solution Here for above question 8:
var=input("Enter any Character : ")
list1=list(var)
word=True
for i in range(len(list1)):
  if list1[i]==" ":
    word=True
  elif word and "a" <=list1[i]<="z":
    list1[i]=chr(ord(list1[i])-32)
    word=False
  else:
    word=False
    var.join(list1)
print(list1)

"""### Question 9: Write a Python program to find the frequency of each character in a string.

- `sample input : `
    - `var = 'sharuk khan'`
- `sample output :`
    - `result : {'s': 1, 'h': 2, 'a': 2, 'r': 1, 'u': 1, 'k': 2, ' ': 1, 'n': 1}`
"""

# Please write The solution Here for above question 9:
var=input("Enter any Character : ")
dict1={}
for char in var:
  if char in dict1:
    dict1[char]+=1
  else:
    dict1[char]=1
print(dict1)

"""### Question 10: write a python programme to find the sum of all the even characters based on Ascii values

- `sample input : `
    - `var = 'sharuk khan'`
- `sample output :`
    - `result : 464`

"""

var=input("Enter any Character : ")
value=0
for char in var:
  ascii=ord(char)
  if ascii%2==0:
    value+=ascii
print(value)