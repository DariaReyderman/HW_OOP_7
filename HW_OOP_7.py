# Exercise 1
def sum_numbers(*args):
    print(sum(args))


# Exercise 2
def print_user_info(**kwargs):
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")


# Exercise 3
def combine_values(*args, **kwargs):
    print(f"Sum: {sum(args)}")
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")


# Exercise 4
def greet_user(**kwargs):
    if 'name' in kwargs:
        print(f"Hello {kwargs['name']}")
    else:
        print("Hello guest")


sum_numbers(1, 2, 3, 4)
print_user_info(name="Dana", age=30, city="Tel Aviv")
combine_values(2, 4, 6, name="Tom", job="Dev")
greet_user(name="Lior")
greet_user()
