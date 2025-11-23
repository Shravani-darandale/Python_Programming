year = int(input("Enter year : "))

#check year is leap year or not

#year divisible by 400 is leap year

# year divisible by 4 but not divisible by 100 is leap year

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")

else:
    print("Not a Leap Year")