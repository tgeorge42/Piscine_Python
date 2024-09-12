# Exercise about the basic types in Python

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# Can change the value of a list, append, remove, etc.
ft_list[1] = "World!"

# Can't change the value of a tuple, so need to erase the old one
ft_tuple = ("Hello", "France!")

# Unique values in a set, can't have duplicates, can't access by index
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Can change the value of a dictionary, add, remove, etc.
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)