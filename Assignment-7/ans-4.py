#python script to print category of person regarding age

age=int(input("Enter age of the person: "))

match age:
    case age if age<10:
        print("Kid")
    case age if age<20:
        print('Teen')
    case age if age <40:
        print('Young')
    case age if age<60:
        print("Experienced")
    case age if age>=60:
        print('Senior Citizen')