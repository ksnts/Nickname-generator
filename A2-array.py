#Assignment 2 Arrays

#Instructions:

#Write a python program that do the following:
#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array

#Pre-determined array
arrayOG=[1,35,28,8,24,16,100,99,20,8]
#Loop condition
Y=0
#Looping menu
while(Y==0):
    print(":::::::::::::::::::::::::::::::")
    print("   Welcome to the Array Menu")
    print(":::::::::::::::::::::::::::::::")
    print("\nThis is the current array: ")
    print(arrayOG)
    print("\nThese are your options:\n *(1) Add an element\n *(2) Insert an element\n *(3) Modify/Change an element\n *(4) Delete an element\n *(5) Arrange array in ascending order\n *(6) Arrange array in descending order\n *(7) Count a number\n *(8) Reverse the array\n *(9) Return an index of a number\n *(10) Find the min and max elements in the array\n *(11) Sums the elements in the array")

    choice=input("\nInput your choice(number): ")
#If else for user input choices (Each if else will process the array and display the result)
    if choice=="1":
        print("\nCurrent Array: ")
        print(arrayOG)
        add=int(input("\nEnter number to add: "))
        arrayOG.append(add)
        print("\n******************RESULT******************\n")
        print(arrayOG)


    elif choice=="2":
        print("\nCurrent Array: ")
        print(arrayOG)
        insertN=int(input("\nEnter number to insert: "))
        insertO=int(input("Enter index for the number to be inserted: "))
        arrayOG.insert(insertO,insertN)
        print("\n******************RESULT******************\n")
        print(arrayOG)


    elif choice=="3":
        print("\nCurrent Array: ")
        print(arrayOG)
        modify1=int(input("\nEnter index of the number to change/replace: "))
        modify2=int(input("Enter new value: "))
        arrayOG[modify1]=(modify2)
        print("\n******************RESULT******************\n")
        print(arrayOG)
        

    elif choice=="4":
        print("\nCurrent Array: ")
        print(arrayOG)
        delete=int(input("\nEnter the number you wish to delete: "))
        arrayOG.remove(delete)
        print("\n******************RESULT******************\n")
        print(arrayOG)
       
    
    elif choice=="5":
        print("\nCurrent Array: ")
        print(arrayOG)
        print("\n*The array will now be be sorted (Ascending)*")
        arrayOG.sort()
        print("\n******************RESULT******************\n")
        print(arrayOG)
        
    
    elif choice=="6":
        print("\nCurrent Array: ")
        print(arrayOG)
        print("\n*The array will now be be sorted (Descending)*")
        arrayOG.sort()
        arrayOG.reverse()
        print("\n******************RESULT******************\n")
        print(arrayOG)
        
    
    elif choice=="7":
        print("\nCurrent Array: ")
        print(arrayOG)
        count=int(input("\nEnter a number to count: "))
        repeated=arrayOG.count(count)
        print("\n******************RESULT******************\n")
        print(f"The array has ({repeated}) of this number")
        

    elif choice=="8":
        print("\nCurrent Array: ")
        print(arrayOG)
        print("\n*The array will now be reversed*")
        arrayOG.reverse()
        print("\n******************RESULT******************\n")
        print(arrayOG)
       
    
    elif choice=="9":
        print("\nCurrent Array: ")
        print(arrayOG)
        indexChoice=int(input("\nEnter a number to show its index: "))
        index=arrayOG.index(indexChoice)
        print("\n******************RESULT******************\n")
        print("The selected number's index is: ", index)
        
    
    elif choice=="10":
        print("\nCurrent Array: ")
        print(arrayOG)
        print("\n*Finding the min and max of the array*")
        min=min(arrayOG)
        max=max(arrayOG)
        print("\n******************RESULT******************\n")
        print(f"The min is {min} and the max is {max}")
        
    
    elif choice=="11":
        print("\nCurrent Array: ")
        print(arrayOG)
        print("\n*Getting the sum of the array*")
        sum=sum(arrayOG)
        print("\n******************RESULT******************\n")
        print("The sum of the array is: ",sum)
        
    #Program will ask the user if they want to continue
    game=int(input("\nPress 1 to continue program: "))
    if game==1:
        print("\n****************CONTINUING****************\n")
    elif game!=1:
        print("\nThank you!")
        Y=1