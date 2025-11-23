import random
game = ("rock","paper","scissor")
score = {"bot": 0,
         "player": 0}
x = input("do you want to play game:(y/n)")
if x.lower() == "y":
    while True:
      player = input("enter your choice: ")
      bot = random.choice(game)
      if player.lower() == "n":
        print(f"player = {score['player']}")
        print(f"bot = {score['bot']}")
        if score["player"] == score["bot"]:
          print("draw")
        elif score["player"] > score["bot"]:
          print("you win")
        else:
          print("you lose")
        print("have a nice day")
        break
      elif player.lower() == bot:
        score["player"] += 1
        score["bot"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("draw")
      elif player.lower() == game[0] and bot == game[1]:
        score["bot"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you lose")
      elif player.lower() == game[0] and bot == game[2]:
        score["player"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you win")
      elif player.lower() == game[1] and bot == game[0]:
        score["player"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you win")
      elif player.lower() == game[1] and bot == game[2]:
        score["bot"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you lose")
      elif player.lower() == game[2] and bot == game[0]:
        score["bot"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you lose")
      elif player.lower() == game[2] and bot == game[1]:
        score["player"] += 1
        print(f"player = {player}")
        print(f"bot = {bot}")
        print("you win")
      else:
        print("choice not avilable")
elif x.lower() == "n":
  print("have a nice day")


















