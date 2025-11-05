#Assignment2_Task2
#Task2: Sum of integer from 1 to 50 using loop
sum=0                                               # variable declared with initial value 0
for i in range(1,50):                               # for loop iteration from range 1 to 50
    sum += i                                        # sum=sum+1 can be written with urinary operator, with each iteration incremental value of i added to variable sum and assign to sum itself.
print(f"The sum of number from 1 to 50 is: {sum}")  # last added value store in variable sum inside for_block is call outside for_block to print.
