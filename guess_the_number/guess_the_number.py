import random

random_number = random.randint(1, 10)
print "Guess the number:(1 - 10)"
tries = int(raw_input("Choose num:"))

while tries != random_number:
    print "Sorry, wrong number"
    tries = int(raw_input("Choose num:"))

print "Correct!"