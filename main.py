# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
logo='''
                      /$$$$$$   /$$$$$$
                     /$$__  $$ /$$__  $$
  /$$$$$$$  /$$$$$$  | $$  \__/| $$  \__//$$$$$$   /$$$$$$
 /$$_____/ /$$__  $$ | $$$$    | $$$$   /$$__  $$ /$$__  $$
| $$       | $$  \ $$| $$_/    | $$_/  | $$$$$$$$| $$$$$$$$
| $$       | $$  | $$| $$      | $$    | $$_____/| $$_____/
|  $$$$$$$|  $$$$$$/ | $$      | $$    |  $$$$$$$|  $$$$$$$
 \_______/ \______/  |__/      |__/     \_______/ \_______/ 
 '''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total_amount=0
def amount():
    global total_amount
    rup=int(input("How many rupees you have? "))
    ath=int(input("How many athanas(50 paise)? "))
    cha=int(input("How many charanas(25 paise)? "))
    pai=int(input("How many paise? "))
    total_amount=rup+(0.5*ath)+(0.25*cha)+(0.01*pai)


def remain():
    global more, wat_re, milk_re, coffee_re
    if add==0:
        wat_re=resources["water"]-MENU[c_type]["ingredients"]["water"]
        milk_re=resources["milk"]-MENU[c_type]["ingredients"]["milk"]
        coffee_re=resources["coffee"]-MENU[c_type]["ingredients"]["coffee"]
    else:
        wat_re-=MENU[c_type]["ingredients"]["water"]
        milk_re-=MENU[c_type]["ingredients"]["milk"]
        coffee_re-=MENU[c_type]["ingredients"]["coffee"]
    if wat_re<0:
        print(f"Sorry there is not enough water!\nPlease put {-1*wat_re}ml of water.")
        wat_re += int(input("How much ml of water you want to input? "))
        if wat_re<0:
            print("Sorry its still less! See you again!")
            more="n"
    if milk_re<0:
        print(f"Sorry there is mot enough Milk!\nPlease put {-1*milk_re}ml of milk.")
        milk_re += int(input("How much ml of milk you want to input? "))
        if milk_re<0:
            print("Sorry its still less! See you again!")
            more="n"
    if coffee_re<0:
        print(f"Sorry there is mot enough coffee!\nPlease put {-1*coffee_re}g of coffee.")
        coffee_re += int(input("How much ml of coffee you want to input? "))
        if coffee_re<0:
            print("Sorry its still less! See you again!")
            more="n"
more="y"
add=0
print(logo)
while (more=="y"):
    global c_type
    c_type=input('Which coffee would you want to drink? "espresso", "latte" or "cappuccino"?').lower()

    if c_type!="latte" and c_type!="espresso" and c_type!="cappuccino":
        print("Please Enter Valid Input!!")
    else:
        remain()
        if more!="n":
            amount()
            cost_=MENU[c_type]["cost"]
            if total_amount<cost_:
                less=cost_-total_amount
                print(f"Please Enter more coins!\nYou are less by Rs.{less}")
                more="n"
            elif total_amount>cost_:
                return_am=total_amount-cost_
                print(f"Here's your {c_type}☕!\nAnd here's your return:- Rs.{return_am}")
            elif total_amount==cost_:
                print(f"Here's your {c_type}☕! Your balance is now nill")
            elif total_amount==0:
                print("Your amount has finished or you haven't inserted sufficient coins! Insert coins for coffee!!"
                      "(Click the play button)")
                more="n"
            print("************************************************")
            more=input("Want more coffee? Type 'Y' if yes, or 'N'. ").lower()
            if more!="y":
                print("See you Again!!!")
            add += 1

