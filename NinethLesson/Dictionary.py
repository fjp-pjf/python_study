# this is basically objects from javascript

family_jargon = {
    "Family": "Consist of Femin, Fenas, Raji and Delna and Terra",
    "Partner": "Someone you want to marry",
    "Partner_name": "Find out already"
}

# to print any value from the dictionary, you can access them with key and its value will be printed
print(family_jargon["Partner"])

# the value can be replaced as well in dictionary
family_jargon["Partner_name"] = "Vimal Sagar Murali"
print(family_jargon)

# if a key we pass does not exist while trying to modify, it will create a new entry
family_jargon["I_want"] = "to be Married and be happy with 3 kids"
print(family_jargon)

