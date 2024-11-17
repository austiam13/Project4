numbers=[]
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInter']
get_user_name=str(input("Please Enter your name: "))

if get_user_name not in usernames:
    print("Access denied")

else:
  print("Access granted")
  for i in range(0,5):
    num=int(input("please enter 5 numbers: "))
    numbers.append(num)

  for i in range(0,5):
    print(f"Number : {numbers[i]}")

  print(f"The first number is : {numbers[0]}")
  print(f"The last number is : {numbers[-1]}")
  print(f"The smallest number is : {min(numbers)}")
  print(f"The largest number is : {max(numbers)}")
  print(f"The average of the numbers is : {sum(numbers)/len(numbers)}")


