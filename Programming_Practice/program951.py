#Problems on Digits
#Accept number for user and display digits seperately

def DisplayDigits(No):
    Digit = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        No = No // 10   #// ---> Floor Division

def main():
    No = 0

    print("Enter number : ")
    No = int(input())

    DisplayDigits(No)   

main()