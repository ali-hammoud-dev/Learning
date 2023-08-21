import functools

user = {"username":"jose","access_level":"admin"}

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user["access_level"] == "admin":
         return func(*args,**kwargs) 
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


@make_secure
def get_admin_password(panel):
    password_dict = {
        "admin": "1234",
        "billing": "super_secure_password"
    }
    
    return password_dict.get(panel, "Invalid panel")

print(get_admin_password(panel = input("Please enter Panel : (Admin or billing)").lower()))

