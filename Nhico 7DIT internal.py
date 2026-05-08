orders = [] 
breads = ["Flatbread", "Pita", "Naan", "Bowl"]

proteins = ["Chicken", "Beef", "Lamb", "Doner", "Falafel", "None"]

vegetables = ["Lettuce", "Tomato", "White onion", "Red onion", "Cucumber", "Pickles"]

sauces = ["Garlic", "Medium chilli", "Hot chilli", "Tzatziki", "Tahini", "Hot garlic"]

MAX_LIMIT = 4

options = {
    1 : breads, 
    2 : proteins,
    3 : vegetables,
    4 : sauces
}

valid_choices = [1, 2, 3, 4]

def view_menu():


    """
    this is to view the menu of ingredients that the customer can choose from
    """
    print("-----MENU-----")
    print(f"\n{breads} \n{proteins} \n{vegetables} \n{sauces}")


def business_menu():


    """
    this is the menu for if the user is part of the business
    """
    print("\n---- BUSINESS MENU ----")
    print("1. View Orders")
    print("2. View Ingredients")
    print("3. Clear all Orders")
    print("4. Exit")

def customer_menu():


    """
    this is the menu for if the user is a customer
    """
    print("\n---- CUSTOMER MENU ----")
    print("1. Order")
    print("2. View Order")
    print("3. View Menu")
    print("4. Exit")

def ingredients_menu(): 


    """
    the menu of the different categories for ingredients
    """
    print("\n1. View Breads")
    print("2. View Proteins")
    print("3. View Vegetables")
    print("4. View Sauces")

def get_int():


    """
    made a function for whenever the user has to type in an integer to be more efficient.
    """
    while True:
        try:
            num = int(input("\nEnter Here: "))
            return num 
            
        except ValueError:
            print("Invalid Input, Try again.")

def add_ingredient(category):


    """
    it adds to the list of the category chosen
    """
    print(category)
    addition = input("What would you like to add?: ").strip().capitalize()
    category.append(addition)
    print(f"New list: {category}")

def remove_ingredient(category):


    """ 
    removes from the category chosen, i made it make sure to test whether the item COULD be removed.
    """
    while True:
        print(category)
        remove = input("What would you like to remove?: ").strip().capitalize()
        
    
    
        try:
            category.remove(remove)
            print(f"New List: {category}")
            break
    
        except ValueError:
            print("Invalid removal, Try again")

def view_category(category):


    """
    when user selects a category they will be able to do either add to it, reove from it or exit
    """
    print("what would you like to do?: ")
    print("1. Add")
    print("2. Remove")
    print("3. Exit")
    
    option = get_int()

    if option == 1:
        add_ingredient(category)

    elif option == 2:
        remove_ingredient(category) # for ingredients that need multiple

def ingredient_order(category): 


    """
    has user choose how many they would like to add, then for how many it loops for them to enter their ingredient.
    """ 
    print(category)
    category_order = []
    print("How many do you want to add to your order?(entering more means added portion (: ) ")
    amount = get_int()
    if amount == 0:
        return []
    elif amount > MAX_LIMIT:
        print(f"Thats too much, maximum is {MAX_LIMIT}, you will only be able to choose {MAX_LIMIT} now.")
        amount = MAX_LIMIT
    


        
    for i in range(amount):
        while True:
            choice = (input(f"Enter ingredient {i+1}: ")).strip().capitalize()
            if choice in category:
                category_order.append(choice)
                print(category_order)
                break
            else: print("Choice is Unavailable, Please pick from selected options")
    return category_order
        

def single_ingredient(category): # for ingredients only needing 1 type


    """
    for single ingredient foods, gets the input and puts it into the list to get put into the dictionary
    """
    while True:
        print(category)
        category_order = []
        user_input = input("Enter Ingredient: ").strip().capitalize()
        if user_input in category:
            category_order.append(user_input)
            
            print(category_order)
            return category_order
        else: 
            print(f"Please Input a proper choice, {user_input} is not valid")

def add_order(orders):


    """
    the code that inserts the ingredients into the dictionary
    """
    orders.append({
        "Bread" : single_ingredient(breads),
        "Proteins" : ingredient_order(proteins),
        "Vegetables" : ingredient_order(vegetables),
        "Sauces" : single_ingredient(sauces)
    })
    print(orders)

def view_orders():
    """ 
    a way to view the orders and remove the orders
    """
    if orders == []:
        print("\nNo orders woohoo!")
        return
        
    else:
        print("----CURRENT ORDERS----")
        for i in range(len(orders)):
                print(f"{i+1}. {orders[i]}")

        print("\nWhat would you like to do?")
        print("1. Finish Order")
        print("2. Exit")

        user_choice = get_int()

        if user_choice == 1:
            print("\nWhich Order would you like to finish?")
            remove_order = get_int()

            if remove_order in range(1, len(orders) + 1):

                try:
                    orders.pop(remove_order - 1) #uses pop instead of remove as it seems more optimal
                    print("Order Removed")
            
                except ValueError:
                    print("Invalid removal, Try again")






def business():
    """
    a function for all business related functions and for the business sid of the code to make the main as simple as possible
    """
    business_menu()
    business_choice = get_int()

    if business_choice == 1:
        view_orders()
        

    elif business_choice == 2:
        print("which would you like to view?")
        ingredients_menu()
        view = get_int()
        if view in options:
            selected_list = options[view]
            print(selected_list)

            view_category(selected_list)
        else: print("Error! please input a proper view category.")
        
    elif business_choice == 3:
        print("Orders CLEARED")
        orders.clear()


    elif business_choice == 4:
        return "exit"
    
    else: print("This is not an Option.")

def customer():
    """
    same but for customers.
    """
    customer_menu()

    customer_choice = get_int()

    if customer_choice == 1:
        add_order(orders)
    
    elif customer_choice == 2:
        for i in range(len(orders)):
            print(f"{i+1}. {orders[i]}")

    elif customer_choice == 3:
        view_menu()
    
    elif customer_choice == 4:
        return "exit"
    
    else: print("This is not an option.")


while True:
    """
    Main code
    """

    print("\nWelcome to Nhico's Kebabs")
    print("Are you a Kebab Warrior or customer?")
    print("1. Kebab Warrior")
    print("2. Customer")
    print("3. Exit")

    initial_choice = get_int()

    if initial_choice == 1:
        while True:
            active = business()
            if active == "exit":
                break



    elif initial_choice == 2:
        while True:
            active = customer()
            if active == "exit":
                break
    
    elif initial_choice == 3:
        print("Thank you!")
        break


