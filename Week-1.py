#!/usr/bin/env python
# coding: utf-8

# # Data Analytics and Machine Learning using Python![image.png](attachment:image.png)

# # Lab Exercise &emsp;   Week-1&emsp; &emsp;Submission Date :- 24 May 2020   Before 6 P.M.

# # Lab-1
# 
# * Create GitHub Account.
# * Clone the repository from………………
# * Add a file to src folder say “Myprofile.txt”
# * Use < git add > command to add that file to the repository.
# * Use command to commit your changes. ( write meaningful message with commit)
# * Use command to send your change in your repository. 
# * Look online and check if changes has been pushed or not.
# 
# 
# #### After completing above steps write your github repository URL Below
# 

# In[2]:


# Write Github URL 


# # Lab-2 
# ### Write a Python program to input a number from the user and check if it is positive, negative or zero.
# 

# In[3]:


n=int(input())
if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative")
else:
    print("The number is zero")


# # Lab-3
# ### Write a Python Program to Find the Largest Among Three Numbers, using the least number of lines of code.
# 

# In[11]:


# Write Your Code Here with Proper Comments
a,b,c=input().split()
if a>b and a>c:
    print(a," is largest")
elif b>a and b>c:
    print(b," is largest")
else:
    print(c," is largest")



# ### Lab-4
# ### Write a Python program to input a month name and print number of days in it.
# 
# Eg., January – 31
# 
# February – 28/29
# 

# In[15]:


# Write Your Code Here with Proper Comments
n=input()
if n=='January' or n=='March' or n=='May' or n=='July' or n=='August' or n=='October' or n=='December':
    print(n,"has 31 days")
elif n=='April' or n=='June' or n=='September' or n=='November':
    print(n,"has 30 days")
elif n=='February':
    print(n,"has 28/29 days")
else:
    print("Not a month")



# # Lab-5
# ### Write a Python Program to Find the Factorial of a Number.
# n! = n * n-1 * n-2 * n-3 * …. *3 * 2 * 1
# 

# In[17]:


# Write Your Code Here with Proper Comments
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print("The factorial of a number is",f)
    



# # Lab-6
# At a certain school, student email addresses end with <b>@student.college.edu</b>, while professor email addresses end with <b>@prof.college.edu</b> 
# 
# Write a program that first asks the user how many email addresses they will be entering, and then has the user enter those addresses.
# 
# After all the email addresses are entered, the program should print out a message indicating either that all the addresses are student addresses or that there were some professor addresses entered.

# In[11]:


# Write Your Code Here with Proper Comments
n=int(input("Enter the number of email addresses"))
s=0
p=0
for i in range(n):
    id=input()
    if 'student' in id:
        s+=1
    if 'prof' in id:
        p+=1
if p==0:
    print("All the addresses are student addresses")
else:
    print("There are some professors addresses entered")
    



# # Lab-7
# ### Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# 
#  Suppose the following input is supplied to the program:
#     
#     without,hello,bag,world
# 
# Then, the output should be:
# 
#     bag,hello,without,world
# 

# In[19]:


# Write Your Code Here with Proper Comments
n=input()
words=[word for word in n.split(",")]
print(','.join(sorted(list(set(words)))))



# # Lab-8
# ### Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000

# In[5]:


# Write Your Code Here with Proper Comments
def showEmployee(n,s=9000):
    return n,s
showEmployee('ishani',50000)
    
    


# # Lab-9
# ### Create an inner function to calculate the addition in the following way
# 
# * Create an outer function that will accept two parameters a and b say <b>outerFun(a, b)</b>
# 
# * Create an inner function(<b>e.g. innerFun(a,b)</b>) inside an outer function that will calculate the addition of a and b 
# * At last, an outer function will add 5 into addition and return it

# In[18]:


# Write Your Code Here with Proper Comments
def outerFun(a,b):
    def innerFun(a,b):
        return a+b
    return a+b+5
outerFun(2,3)
    


# # Lab-10
# ### Assign a different name to function and call it through the new name
# 
# Below is the function displayStudent(name, age). Assign a new name showStudent(name, age)  to it and call through the new name

# In[29]:


# Write Your Code Here with Proper Comments
def displayStudent(name,age):
    return name,age
displayStudent.__name__='showStudent'
showStudent('ishani',20)


# # Lab-11
# Write a program that gets a string from the user containing a potential telephone number.The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. 
# 
# A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk. 
# 
# The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct.
# 
# Test your program with the output shown below.
# 
# Enter a phone number: 301-447-5820
# 
# Valid
# 
# Enter a phone number: 301-4477-5820
# 
# Invalid
# 
# Enter a phone number: 3X1-447-5820
# 
# Invalid
# 
# Enter a phone number: 3014475820
# 
# Invalid

# In[25]:


# Write Your Code Here with Proper Comments
id=input()
c=0
d=0
_1=0
for i in id:
    if i.isdigit():
        d+=1
    elif i=='-' and d==3:
        _1+=1
    elif(i=='-') and d==6 and _1==1:
        pass
    else:
        c=1
if c==0:
    print("Valid")
else:
    print("Invalid")


# In[ ]:




