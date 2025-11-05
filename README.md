# Assignment2-Module3-Control-structure-in-Python
# Assignment 2_Task1.

# Task 1: Check if a Number is Even or Odd

## line1:    **num = int(input("Enter a number: "))**

num is taken as variable which will get value from user through input function, comment is mentioned inside input function for user interaction i.e 'Enter the a number'. input() typecast to integer  so that is assigned with integer value only.


## lin2:      **if num % 2 == 0:**

if statement start , with condition  having logic  to check even odd by dividing value of variable num by 2 using modulus operator %.Since division using % operator gives remainder only. So Even number are divisible by 2 i.e give remainder 0 , equality == operator used to check resultant remaider is 0 or not. If remainder is 0  the condition will be True otherwise False.


## line3:     **print(f"{num} is a even number")**

if Block start  with indentation 4 space  indicate the start of if block. print() execute when condition mentioned in if statement is True . print() used to print value of variable num along with string statement using fstring. After execution of if statement control comes out of if_else block.


## line4:      **else:**

else statement start without indentation using keyword else:

## line5:      **print(f"{num} is a odd number")**

else_block start  with indentation of 4 spaces. print() execute when condition mentioned in if statement is False . print() used to print value of variable num along with string statement using fstring.                                                                                                                                                                                                                                                                                              


                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                    

# Assignment 2_Task2.

# Task 2: Sum of Integers from 1 to 50 Using a Loop

## line1 :     sum=0 

Variable sum declared with initial value 0 before start of loop so that it act as container of sum of iteration value and updated value of variable sum. if sum=0 declared inside the loop then with every iteration the value of variable sum become 0 and final value also will be 0+50 i.e 50 which will be incorrect answer.


## line 2:      for i in range(1,50):

for loop start taking iteration variable i , number of loop going to iterate fixed between 1 to 50  using range().


## line 3:       sum += i

start with indentation 4 space after for_statement  indicate the start of for block .  sum += i which mean sum=sum+i  . With each iteration incremental value of i added with the value of variable sum and reassign to variable sum itself as per logic. The updated value of sum get added with next incremental value of i on next iteration and again reassign to sum itself.This process repeat till 50 iteration and finally updated value in variable sum will be the sum of integer from 1 to 50. 


## line4:     print(f"The sum of number from 1 to 50 is: {sum}")

last added value store in variable sum inside for_block is called outside for_block to print along with string statement using fstring.
            

