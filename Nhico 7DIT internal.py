orders = [] 
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

def ingredient_order(category): #for ingredients that need more than 1 
    print(category)
    category_order = []
    amount = int(input(f"How many do you want to add to your order?: "))

    for i in range(amount):
        category_order.append((input(f"Enter ingredient {i+1}: ")))
        print(category_order)

    return category_order

def add_order(orders):
    orders.append({
        "Bread" : ingredient_order(breads), 
        "Proteins" : ingredient_order(proteins),
        "Vegetables" : ingredient_order(vegetables),
        "Sauces" : ingredient_order(sauces)
    })







while True: #maybe make this into a function
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
        

    
