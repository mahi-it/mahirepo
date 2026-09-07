print("Welcome to the Data Analyzer and Transformer Program !")

while True :
     print()
     print("Main Menu :")
     print("1. Input Data")
     print("2. Display Data Summary(Built-in Function)")
     print("3. Calculate Factorial(Recursion)")
     print("4. Filter Data by Threshold(lambda Function)")
     print("5. Sort Data")
     print("6. Display Dataset Statistics(Return Multiple Values)")
     print("7. Exit Program")
     choice=int(input("Please enter your choice : "))

     

     match choice :
         case 1 : 
               print()
               
               def add_values(*args):
                     '''This function takes multiple values from user'''
                     global arr
                     arr=[]
                     return args 
              
               element=list(map(int,input("Enter data for a 1D array(separated by space) :").split()))
                
               arr =list(add_values(*element))
               
               print("----",add_values.__doc__,"----")
               print()
               print("Data has been stored successfully !")
               
               print(arr)
               
         case 2 :
               print()
               if(len(arr)==0):
                    print("Enter the data first !")
               else :  
                  print("Total element :", len(arr))
                  print("Maximum value :",max(arr))
                  print("Minimum value :",min(arr))
                  print("Sum of all the value :",sum(arr))
                  print("Average value :",sum(arr)/len(arr))
        
         case 3 :
               print()
               n=int(input("Enter a number to calculate its factorial : "))
               def fact(n):
                     if(n==1):
                        return 1 
                     elif(n==0):
                        return 1
                     else:
                        return n*fact(n-1)
               print(f"Factorial of {n} is :", fact(n)) 

         case 4 :
               print()
               if(len(arr)==0):
                    print("Enter the data first !")
               else :    
                  n=int(input("Enter a threshold value to filter out data above this value :"))
                  numbers = list(filter(lambda x:x>n,arr))
                  print(f"Filtered Data (value > {n} :)",end=" ")
                  print(*numbers,sep=",")

         case 5 :
                  print()
                  if(len(arr)==0):
                     print("Enter the data first !")

                  else : 
                        print("choose sorting option :")
                        print("1.Ascending")
                        print("2.Descending")

                        choose=int(input("Enter your choice : "))
                        
                        match choose :
                              case 1 :
                                    print()
                                    arr.sort()
                                    print("Sorted Datan in Ascending Order :\n",arr)
                              case 2 :
                                    print()
                                    arr.sort(reverse=True)
                                    print("Sorted Datan in Descending Order :\n",arr)
                              case _ :
                                    print("invalid choice")
                          
         case 6 :
                  print()
                  if(len(arr)==0):
                     print("Enter the data first !")
                  else : 
      
                    print("Dataset Statistics :")
                  data={
                        "Minimum value:" : min(arr),
                        "Maximum value :" : max(arr),
                        "Sum of all value :":sum(arr),
                        "Average value :" : sum(arr)/len(arr)
                  }
                  def stat(**kwargs):
                        
                        for key, value in kwargs.items():
                          print(key, value)
                  
                  stat(**data)
                                      
         case 7 :
                print()
                print("Thank you for using the Data Analyzer and Transformer Program. Goodbye !")
                break
         case _ :
                print("Invalid Choice , Please choose between (1-7)")
     
        