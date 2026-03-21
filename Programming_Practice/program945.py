# Accept number for user and check wheather the number is even or odd 

def CheckEven(No):
    if(No % 2 == 0):
        print("Number is even")

    else:
        print("Number is odd")    


def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    CheckEven(Value)

main()