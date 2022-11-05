#Assignment 2 Arrays

#Instructions:

#Write a python program that do the following:
#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array

arrayOG=[1,35,28,8,24,16,100,99,20,8]

Y=0

while(Y==0):

    print("Welcome to the Array Menu")
    print("This is the current array: ")
    print(arrayOG)
    print("These are your options:\n *(1) Add an element\n *(2) Insert an element\n *(3) Modify/Change an element\n *(4) Delete an element\n *(5) Arrange array in ascending order\n *(6) Arrange array in descending order\n *(7) Count a number\n *(8) Reverse the array\n *(9) Return an index of a number\n *(10) Find the min and max elements in the array\n *(11) Sums the elements in the array")

    choice=input("Input your choice: ")

    if choice=="1":
        print("Current Array: ")
        print(arrayOG)
        add=int(input("What number will you add? "))
        arrayOG.append(add)
        print(arrayOG)
                  
    elif choice=="2":
        print("Current Array: ")
        print(arrayOG)
        insertN=int(input("What element will you insert: "))
        insertO=int(input("In what index will the number be inserted?"))
        arrayOG.insert(insertO,insertN)
        print(arrayOG)


    elif choice=="3":
        print("Current Array: ")
        print(arrayOG)
        modify1=int(input("What index will you change/replace? "))
        modify2=int(input("What will be the new value? "))
        arrayOG[modify1]=(modify2)
        print(arrayOG)
        

    elif choice=="4":
        print("Current Array: ")
        print(arrayOG)
        delete=int(input("Enter the number you wish to delete: "))
        arrayOG.remove(delete)
        print(arrayOG)
       
    
    elif choice=="5":
        print("Current Array: ")
        print(arrayOG)
        print("*The array will now be be sorted (Ascending)*")
        arrayOG.sort()
        print(arrayOG)
        
    
    elif choice=="6":
        print("Current Array: ")
        print(arrayOG)
        print("*The array will now be be sorted (Descending)*")
        arrayOG.sort()
        arrayOG.reverse()
        print(arrayOG)
        
    
    elif choice=="7":
        print("Current Array: ")
        print(arrayOG)
        count=int(input("Enter a number to count: "))
        repeated=arrayOG.count(count)
        print(f"The array has ({repeated}) of this number")
        

    elif choice=="8":
        print("Current Array: ")
        print(arrayOG)
        print("*The array will now be reversed*")
        arrayOG.reverse()
        print(arrayOG)
       
    
    elif choice=="9":
        print("Current Array: ")
        print(arrayOG)
        indexChoice=int(input("Enter a number to show its index: "))
        index=arrayOG.index(indexChoice)
        print("The selected number's index is: ", index)
        
    
    elif choice=="10":
        print("Current Array: ")
        print(arrayOG)
        print("*Finding the min and max of the array*")
        min=min(arrayOG)
        max=max(arrayOG)
        print(f"The min is {min} and the max is {max}")
        
    
    elif choice=="11":
        print("Current Array: ")
        print(arrayOG)
        print("*Getting the sum of the array*")
        sum=sum(arrayOG)
        print("The sum of the array is: ",sum)
        
    
    game=int(input("Continue program: "))
    if game==1:
        print("**")
    elif game!=1:
        Y=1






    



