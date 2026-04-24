orders = [{},{}] 
breads = ["Flatbread", "Pita", "Naan", "Bowl"]

proteins = ["Chicken", "Beef", "Lamb", "Doner", "Falafel", "None"]

vegetables = ["Lettuce", "Tomato", "White Onion", "Red Onion", "Cucumber", "Pickles"]#Make sure on order it asks how many veges they want

sauces = ["garlic", "medium chilli", "hot chilli", "tzatziki", "Tahini", "Hot garlic"]


def business_menu():
    print("---- BUSINESS MENU ----")
    print("1. View Orders")
    print("2. View Ingredients")
    print("3. Exit")


def ingredients_menu(): #when viewing each category 
    print("1. View Breads")
    print("2. View Proteins")
    print("3. View Greens")
    print("4. View Sauces")


def view_category(category):
    print(category)
    print("1. Add")
    print("2. Remove")
    print("3. Exit")


def add_ingredient(category):
    print(category)
    addition = input("What would you like to add?: ")
    category.append(addition)

def remove_ingredient(category):
    print(category)
    remove = input("What would you like to remove?: ")
    
    try:
        category.remove(remove)

    
    except ValueError:
        print("Invalid removal, Try again")


