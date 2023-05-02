#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# 2.Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3.Write a Python Program to Check Leap Year?

# In[3]:


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# 4.Write a Python Program to Check Prime Number?

# In[15]:


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[13]:


for num in range(1, 10001):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# In[ ]:




