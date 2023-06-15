def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=25, city="New York")
# Output:
# name: John
# age: 25
# city: New York
