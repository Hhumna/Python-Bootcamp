name1 = input("Name1: ")
name2 = input("Name2: ")
combined = (name1 + name2).lower()

t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e1 = combined.count("e")
total_true = t + r + u + e1

l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e2 = combined.count("e")
total_love = l + o + v + e2

love_score = int(str(total_true) + str(total_love))

if (love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (40 <= love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
