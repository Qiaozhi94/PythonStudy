product_list = [
    ("iphone",5800),
    ("Mac pro",9800),
    ("Bike",800),
    ("watch",10600),
    ("alex Python",120),
]

shopping_list = []

salary = input("your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item),item)

        user_choice = input("要买的商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]

                if p_item[1]<= salary:
                    shopping_list.append(p_item)

                    salary -= p_item[1]

                    print("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m"%(p_item,salary))

                else:
                    print("sorry")
            else:
                print("product code is not exist")

        elif user_choice == "q":

            print("-------shopping list---------")
            for p in shopping_list:
                print(p)
            print("your current balance:", salary)


            exit()

        else:
            print("invalid option")