#购物车程序

_username = "1"
_password = "2"
_shopping_list = ["Iphone  5800","Macbook Pro  12000","Ipad Pro  8000", "Microsoft Surface Pro  100000","Coca Cola  3","Airpods Pro  1999","Milamp  300"]

username = input("username:")
password = input("password:")

count = 0

while count <2:


       if username == _username and password == _password:

          print("welcome! Let's start shopping")
          salary = input("your salary:")
          print("Here is the shopping list:")
          print("1.",_shopping_list[0])
          print("2.",_shopping_list[1])
          print("3.",_shopping_list[2])
          print("4.",_shopping_list[3])
          print("5.",_shopping_list[4])
          print("6.",_shopping_list[5])
          print("7.",_shopping_list[6])
          print("which one do you want to buy?")
          number = input("Number:")
          if int(number) ==1 and int(salary) >5800:

            print("added [iphone] to your shopping cart")
            print("Your Balance:",int(salary)-5800)

          if int(number) == 1 and int(salary) == 5800:

              print("added [iphone] to your shopping cart")
              print("Your Balance:", 0)
              print("Your have successfully Bought Iphone")

          if int(number) == 1 and int(salary) < 5800:

            print("Your don't have enough money! Please choose other items")

          if int(number) ==2 and int(salary) >12000:

              print("added [Macbook Pro] to your shopping cart")
              print("Your Balance:",int(salary)-12000)

          if int(number) ==2 and int(salary) >12000:
              print("Your don't have enough money! Please choose other items")

          if int(number) ==3 and int(salary) >8000:
              print("added [Ipad Pro] to your shopping cart")
              print("Your Balance:", int(salary) - 8000)








          break









       else:

          print("invalid username or password and please try again!")
          username = input("username:")
          password = input("password:")
          count = count + 1


if count == 2:


  print("Your have tried many times and please try later")