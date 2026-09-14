count = 1
total = 0
#BUG added a colon at the end of the while lop to fix syntax error
#BUG i adjusted the while loop condition to count <= 5: so that the loop would include the nu,ber 5 and print the correct total sum of 15
while count <= 5:
    total = total + count
    count = count + 1
#BUG converted the total variable intop a string in the print statement so that it can join properly with the text
print("Sum of 1 to 5 is: " + str(total))