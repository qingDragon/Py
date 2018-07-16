import time

user,password = "yanz","abc123"
def auth(auth_type):
    def outwapper(func):
        def wapper(*args,**kwargs):
            if auth_type == "local":
                username = input("username:").strip()
                Password = input("password:").strip()
                if username ==user and password==Password:
                    print("user has passed authentication")
                    res = func(*args, **kwargs)
                    print("------------")
                    return res
                else :
                    exit("Invalid username or password")
            elif auth_type == "ldap":
                print("没有ldap,fuck off")
        return wapper
    return outwapper


def index():
    print("welcome to index page")
@auth(auth_type = "local")
def home():
    print("welcome to home page")
    return "from home"
@auth(auth_type = "ldap")
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()