print("Welcome to Personal Journal Manager!")
print("Please select an option:")

while(True):
    print()
    print("1.Add a New Entry")
    print("2.View All Entries")
    print("3.Search for an Entry")
    print("4.Delete All Entries")
    print("5.Exit")
    
    option=int(input("User Input : "))

    match option:
        case 1:
            entry= input("Enter your journal entry:\n")
            with open("my.txt","a") as file:
                file.write(entry + "\n") 
            print("\nEntry added successfully!")
        case 2:
            if():
                with open("my.txt","r") as file:
                    data=file.read()
                    print(data)
            else:
                print("No journal entries found. Start by adding a new entry!")
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("Invalid option.Please select a valid option from the menu")