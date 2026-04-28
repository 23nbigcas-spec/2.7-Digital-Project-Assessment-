orders = [{},{}] 
breads = ["Flatbread", "Pita", "Naan", "Bowl"]

proteins = ["Chicken", "Beef", "Lamb", "Doner", "Falafel", "None"]

vegetables = ["Lettuce", "Tomato", "White Onion", "Red Onion", "Cucumber", "Pickles"]#Make sure on order it asks how many veges they want

sauces = ["garlic", "medium chilli", "hot chilli", "tzatziki", "Tahini", "Hot garlic"]

options = {
    "breads" : breads, 
    "proteins" : proteins,
    "vegetables" : vegetables,
    "sauces" : sauces
}

def business_menu():
    print("---- BUSINESS MENU ----")
    print("1. View Orders")
    print("2. View Ingredients")
    print("3. Exit")

def ingredients_menu(): #when viewing each category 
    print("1. View Breads")
    print("2. View Proteins")
    print("3. View Vegetables")
    print("4. View Sauces")

def get_int():
    while True:
        try:
            num = int(input("Enter Here: "))
            return num 
            
        except ValueError:
            print("Invalid Input, Try again.")

def get_category():
    while True:
        try:
            category = input("Enter Here:")
            return category
        except ValueError:
            print("Invalid Input, Try again")

def add_ingredient(category):
    print(category)
    addition = input("What would you like to add?: ")
    category.append(addition)

def remove_ingredient(category):
    print(category)
    remove = input("What would you like to remove?: ")
    
    
    try:
        category.remove(remove)
        print(f"New List: {category}")
    
    except ValueError:
        print("Invalid removal, Try again")

def view_category(category):
    print("what would you like to do?: ")
    print("1. Add")
    print("2. Remove")
    print("3. Exit")
    
    option = get_int()

    if option == 1:
        add_ingredient(category)

    elif option == 2:
        remove_ingredient(category)




while True: #main line of code
    business_menu()

    business_choice = get_int()

    if business_choice == 1:
        print(orders)

    elif business_choice == 2:
        print("which would you like to view?")
        ingredients_menu()
        view = get_category()
        selected_list = options[view]
        print(selected_list)

        view_category(selected_list)
        

    
