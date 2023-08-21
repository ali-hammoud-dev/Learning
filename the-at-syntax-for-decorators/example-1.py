import functools

user = {"username":"jose","access_level":"admin"}

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

def secure_function(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
         return func() 
        else:
            return f"No admin permissions !"
    return secure_function

@secure_function
def get_admin_password():
    return "1234"

# get_admin_password = secure_function(get_admin_password)
# print(get_admin_password.__name__)
print(get_admin_password())

