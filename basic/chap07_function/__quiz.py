MALE_CONSTANT = 0.0022
FEMALE_CONSTANT = 0.0021


def std_weight(height, gender):
    if gender == "male":
        return height * height * MALE_CONSTANT
    elif gender == "female":
        return height * height * FEMALE_CONSTANT
    else:
        return "error"
    
height = 173
gender = "male"

print(std_weight(height, gender))