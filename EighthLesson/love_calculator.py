first_name = input("Name of the first person")
second_name = input("Name of the second person")


def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)
    
    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)
    
    final_score = int(str(true_score) + str(love_score))
    
    print(f"Your love score is {final_score}")

calculate_love_score(first_name, second_name)
