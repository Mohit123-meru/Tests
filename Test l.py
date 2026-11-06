secret = 23
n = 0
print (" You have ❤️ ❤️ ❤️ ❤️ ❤️  lives")
for n in "23": 
 n = int(input("Guess the number between 1 and 100: "))
 if n <= 22:
        print ("You are 🔥 hot.")
        n = int(input("Guess the number between 1 and 100: "))
 elif n >= 24 and n <= 35:
        print ("You are 🔥 hot.")
        n = int(input("Guess the number between 1 and 100: "))
 elif n >= 36 and n<= 50:
        print ("You are 🌡️ warm.")
        n = int(input("Guess the number between 1 and 100: "))
 elif n >= 51 and n <= 80:
        print ("You are 🥶 cold.")
        n = int(input("Guess the number between 1 and 100: "))
 elif n >= 81 and n <= 100:
        print ("You are 🧊 ice cold.")
        n = int(input("Guess the number between 1 and 100: "))
 else :
        print ("Congrats you guessed the secret number!")
        break