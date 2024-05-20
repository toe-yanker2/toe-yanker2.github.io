import random


def input_float(prompt):
  user_input = ""
  while not isinstance(user_input, float):
    user_input = input(prompt)
    try:
      user_input = float(user_input)
    except ValueError:
      print("Invalid answer!")
  return user_input

if input("Hardmode? (y for yes): ") == "y":
  print("Random float created! Good luck :)")
  random_number = random.uniform(1, 100)
else:
  print("Random integer created!")
  random_number = random.randint(1, 100)
# print(random_number)

guess = -1
while guess != random_number:
  guess = input_float("Guess a number between 1 and 100: ")
  if guess < random_number:
    print("higher!")
  elif guess > random_number:
    print("lower!")
print(f"You Guessed Correctly! The number was {random_number}")