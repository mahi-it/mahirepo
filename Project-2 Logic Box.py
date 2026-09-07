print("Welcome to the Pattern Generator and Number Analyzer !")
while True :
     print()
     print("Select an option :")
     print("1. Generate  a Pattern")
     print("2. Analyze a Range of Numbers")
     print("3. Exit")
     choice=int(input("Enter your choice : "))

     match choice :
         case 1 :
             n =int(input("enter  the number of rows for patterns: "))
             print()
             print("pattern : ")
             for i in range(1,n+1):
                for j in range(i):
                 print("*",end=" ")
                print()
                
         case 2 :
             print()
             a= int(input("enter the start of the range :"))
             b= int(input("enter the end of the range :"))
             for i in range(a,b+1):
                 if(i%2==0):
                     print(f'Number {i} is even')
                 else:
                     print(f'Number {i} is odd ')
             print(f'sum of all numbers from {a} to {b} is :', sum(range(a,b+1)))

         case 3 :
             print("Exiting the program , Goodbye ! ")
             break 
         case _:
             print("invalid choice")