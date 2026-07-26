def age_categorization(age):
    if age <13:
        print ("Child")

    elif age >=13 and age <= 19:
        print("Teenager")

    elif age >=20 and age <=59:
        print ("Adult")
    elif age >=60:
        print("Senior")



age = int(input("Give me age of the person "))

age_categorization(age)
