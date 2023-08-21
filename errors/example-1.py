def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0.")
    return dividend/divisor


students = [
    {"name":"ali","grades":[100,200]},
    {"name":"hsen","grades":[200,300]},
    {"name":"hammoud","grades":[100,200]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades),len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
   print(f"ERROR: {name} has no grades!")
else: ## if no error in try 
    print("-- All student averages calcualted --")
finally: ## all cases will run
    print("-- All student averages calculated !")

# grades =[1,2,3]

# try:
#     avg = divide(sum(grades),len(grades))
# except ZeroDivisionError as e:
#     print(f"there are no grades yet in your lists : {e}")
# else:
#     print(avg)
# finally:
#     print("Thansk!")
