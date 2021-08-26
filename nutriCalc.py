import sys

print("Hello, Welcome to NutriCalc!")

calories = int(input("Enter your budgeted daily calorie intake: "))

print("Do you know your item's macro information?")
ans1 = input("Enter y/n or yes/no")
if eval(ans1 == "y" or "yes"):
    print("Enter your item's macro information (carbs, fats, and protein): ")
    x = int(input("Enter the item's carb count: "))
    y = int(input("Enter the item's fat count: "))
    z = int(input("Enter the item's protein count: "))
if eval(ans1 == "n" or "no"):
    print("Do you know the calorie count of your item?")
    if ans1 == "y" or "yes":
        ans2 = input("Enter your item's calorie content")
    else:
        print("You will need to know either calorie count or the macros of your item. Good bye.")
else:
    print("Enter a valid response.")
    sys.exit()


def calcalc(f=9, c=4, p=4):
    cal = (c * x) + (f * y) + (p * z)
    return cal


def remainingcals():
    remain = calories - calcalc()
    return remain


if remainingcals() > 0:
    print("This item is approximately "+str(calcalc())+" calories and you have "+str(remainingcals()).format(0,000)+" left after this meal based on your caloric budget")
if remainingcals() == 0:
    print("You currently have no calories remaining for the day")
if remainingcals() < 0:
    print("You are over your daily calorie budget by "+str(abs(remainingcals()))+" calories")


# masterFrame = tk
# pane = Frame(masterFrame)
# pane.pack()
#
# top = tk.Tk()
#
# b = tkinter.Button(top, text = "same thing we do every night pinky")
