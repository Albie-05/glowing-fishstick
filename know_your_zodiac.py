
know_your_zodiac = input("do you want to know your zodiac sign? ")

if know_your_zodiac.lower() != "yes":
    quit()

print("okay ! Lets play: ) ")


user_name = input("enter your name: ")
user_age = input("enter your age: ")
user_birth_month = input("enter your birth month: ")
user_birth_date = int(input("enter your birth date: "))

if user_birth_month == "december":
    astro_sign = "sagittarius" if (user_birth_date < 22) else "capricorn"
elif user_birth_month == "january":
    astro_sign = "capricorn" if (user_birth_date < 20) else "aquarius"
elif user_birth_month == "february":
    astro_sign = "Aquarius" if (user_birth_date < 19) else "pisces"
elif user_birth_month == "march":
    astro_sign = "pisces" if (user_birth_date < 21) else "aries"
elif user_birth_month == "april":
    astro_sign = "aries" if (user_birth_date < 20) else "taurus"
elif user_birth_month == "may":
    astro_sign = "taurus" if (user_birth_date < 21) else "gemini"
elif user_birth_month == "june":
    astro_sign = "gemini" if (user_birth_date < 21) else "cancer"
elif user_birth_month == "july":
    astro_sign = "cancer" if (user_birth_date < 23) else "leo"
elif user_birth_month == "august":
    astro_sign = "leo" if (user_birth_date < 23) else "virgo"
elif user_birth_month == "september":
    astro_sign = "virgo" if (user_birth_date < 23) else "libra"
elif user_birth_month == "october":
    astro_sign = "libra" if (user_birth_date < 23) else "scorpio"
elif user_birth_month == "november":
    astro_sign = "scorpio" if (user_birth_date < 22) else "sagittarius"
else:
    print("error")


print(user_name + " your zodiac sign is " + astro_sign)
