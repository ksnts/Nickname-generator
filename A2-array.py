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
    print("This is the original 10 digit array: ")
    print(arrayOG)
    print("These are your options:\n *(1) Add an element\n *(2) Insert an element\n *(3) Modify/Change an element\n *(4) Delete an element\n *(5) Arrange array in ascending order\n *(6) Arrange array in descending order\n *(7) Count repeating numbers\n *(8) Reverse the array\n *(9) Return an index of a number\n *(10) Find the min and max elements in the array\n *(11) Sums the elements in the array")

    choice=input("Input your choice: ")

    if choice=="1":
        add=int(input("What element/number will you add? "))
        arrayOG.append(add)
        print(arrayOG)

        Y=1

    elif choice=="2":
        insertN=int(input("What element will you insert: "))
        insertO=int(input("In what index will the number be inserted?"))
        arrayOG.insert(insertO,insertN)
        print(arrayOG)
        Y=1

    elif choice=="3":
        print(arrayOG)
        modify1=int(input("What index will you change/replace? "))
        modify2=int(input("What will be the new value? "))
        arrayOG[modify1]=(modify2)
        print(arrayOG)
        Y=1

    elif choice=="4":
        



    



