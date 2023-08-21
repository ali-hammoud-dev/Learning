def secure_function(func):
    def wrapper():
        if input("Enter password: ") == get_admin_password():
            func()
        else:
            print("Access denied.")
    return wrapper

@secure_function
def sensitive_operation():
    print("Access granted. Performing sensitive operation.")

def get_admin_password():
    return "1234"

sensitive_operation()