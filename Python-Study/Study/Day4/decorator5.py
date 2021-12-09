import time

user = "georgel"
password1 = "123"

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()

        if username == user and password == password1:
            print("welcome logging in")
            func(*args,**kwargs)

        else:
            print("invalid username or password")

    return wrapper

def index():
    print("welcome to the index page!")

@auth(auth_type = "local")
def home():
    print("welcome to the home page!")


@auth(auth_type = "idap")
def bbs():
    print("welcome to the bbs page")



index()
home()
bbs()