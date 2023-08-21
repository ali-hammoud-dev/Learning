user = {"username":"jose","access_level":"guest"}

def get_admin_password():
    return "1234"

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

def secure_function(func):
## get_admin_password will be equal to this dunction below :
    def secure_function():
        if user["access_level"] == "admin":
         return func() ## this func() ==> main function ==> get_admin_password
        else:
            return f"No admin permissions !"
    return secure_function

get_admin_password = secure_function(get_admin_password)
# user = {"username":"jose","access_level":"admin"}
print(get_admin_password())

# if user["access_level"] == "admin":
#     print(get_admin_password())