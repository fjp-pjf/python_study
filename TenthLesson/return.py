# write a small function that capitalises the string and use return as well

def capitalize_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "invalid input of First name or Second name"
    capitalized_f_name = f_name.title()
    capitalized_l_name = l_name.title()

    return f"Your capitalized name is {capitalized_f_name} {capitalized_l_name}"

print(capitalize_name(f_name= "femin", l_name= "justin"))