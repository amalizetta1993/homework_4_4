def longest_word(*args):
    print(args)
    print(type(args))
    leader = ""
    for word in args:
        if len(word) > len(leader):
            leader = word
    return leader
print(longest_word([1,2], ["a", "b", "c"], [3]))


def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["surname"])
    print(kwargs["age"])
    print(kwargs["phone"])
get_personal_data(name = "Aleksandra", surname = "Kamchenkova", age = 31, phone = +7910)

def my_space_address(*args, **kwargs):
    print(type(args))
    print(args)
    for item in args:
        print(item)
    print()
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
my_space_address("Александра", 31, planet = "Земля", star = "Солнце")
