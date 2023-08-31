
#Write a program that asks a fisher the length of a zander in centimeters.............

zander =float(input("please insert length of zander in centimeter = "))
limit= 42-zander
if zander >= 42:
    print(" zander fulfill the size limit ")
else:
    print("zander does not fulfill the size limit. Please release the fish back to the lake. The fish is", limit, "cm shorter than limit.")


#Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution...............

name = input("Enter cabin class (in block) =  ")
if name == ("LUX"):
    print("upper-deck cabin with a balcony.")
elif name ==("A"):
    print("above the car deck, equipped with a window.")
elif name==("B"):
    print("windowless cabin above the car deck.")
elif name ==("C"):
    print("windowless cabin below the car deck.")
else:
    print("INVALID CABIN CLASS")

#Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high....................

gender=input("Input your gender (M for male and F for female) = ")
HV=float(input("Hemoglobin value(g/l) = "))
if gender == "M" :
    if 134 <= HV <= 167:
        print("NORMAL")
    elif HV < 134 :
        print("LOW")
    else:
        print("HIGH")
elif gender == "F":
    if 117 <= HV <= 155:
        print("NORMAL")
    elif HV < 117:
        print("LOW")
    else:
        print("HIGH")
else:
    print("INVALID GENDER. Input your gender (M for male and F for female)")

#Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400..

year = int(input("ENTER YEAR "))
if ((year % 400 == 0) or
        (year % 100 != 0) and
        (year % 4 == 0)):
    print("Leap Year")
else:
    print("Not leap year")


