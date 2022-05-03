#!/usr/bin/env python
# coding: utf-8

# In[8]:


def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2 
print("Enter the operation u want to perform choose\n"       "1.Add"       "2.Substraction"       "3.Multiplication"       "4.Divide")
select = int(input("select operation u want to perform from 1 2 3 4 :"))
num_1 = int(input("enter 1st element"))
num_2 = int(input("enter 2nd element"))
if select==1:
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif select==2:
    print(num_1, "-", num_2, "=", substract(num_1,num_2))
elif select ==3:
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))
elif select==4:
    print(num_1, "/", num_2, "=", divide(num_1,num_2))
else:
    print("Invalid output")
    


# In[6]:


# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" 		"1. Add\n" 		"2. Subtract\n" 		"3. Multiply\n" 		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")


# In[ ]:




