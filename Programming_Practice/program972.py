#Problems on String
#Count capital letters
#ASCII value are not directly supported by python


def CountCapital(Brr):
   iCount = 0
   for ch in Brr:
      if(ord(ch)[ch] >= 65 and ord(ch)[ch] <= 91): #ISSUE
         iCount = iCount + 1
         
   return iCount


def main():
   print("Enter String : ")
   Arr = input()

   Ret = CountCapital(Arr)

   print("Number of capital characters are : ",Ret)
   
main()