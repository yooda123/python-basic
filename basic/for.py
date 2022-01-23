# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
  print(fruit)

for char in "Hello world!":
  print(char)

# challeng 1
fruits = ['apple', 'peach', 'grapes', 'banana']
favorite = input("好きなフルーツは何ですか？\n")

for fruit in fruits:
  # print(fruit)
  if favorite == fruit:
    print("好き")
  else:
    print("好きではない")


# challeng 2
fruits = ['apple', 'peach', 'grapes', 'banana']
print("'yes' or 'no'で応えてください")
likes = []
dislikes = []
for fruit in fruits:
  # print(fruit)
  answer = input(f"{fruit}は好きですか？")
  if answer == 'yes':
    likes.append(fruit)
  else:
    dislikes.append(fruit)

print(f"""
  あなたの好きなフルーツはこちら: {likes}
  あなたの好きではないフルーツはこちら: {dislikes}
  """)
