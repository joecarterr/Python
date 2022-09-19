# welcome
print("Welcome to the Love Calculator!")

# setting start
loveScore = 0

# questioning
name1 = input("What is your name?:\n")
print(f"Hi {name1} I like your name!\n")
name2 = input("What is their name?:\n")
print(f"Wow, {name2} that's a nice name1\n")

combinedNames = name1 + name2
lowerCase = combinedNames.lower()

# checking for letters in
t = lowerCase.count('t')
r = lowerCase.count('r')
u = lowerCase.count('u')
e = lowerCase.count('e')

true = t + r + u + e

l = lowerCase.count('l')
o = lowerCase.count('o')
v = lowerCase.count('v')
e = lowerCase.count('e')

love = l + o + v + e

realLove = str(true) + str(love)

if realLove >= str(90):
    print("You guys are true lovers!")
    print(f"You had a score of {realLove}")
    quit()
elif str(40) <= realLove <= str(50):
    print("You guys are okay together")
    print(f"You had a score of {realLove}")
else:
    print(f"Your score was {loveScore}, you're not very well matched!")

