import sqlite3

groceries = [
  "apples",
  "bananas",
  "clementines",
  "dill",
  "eggs",
  "flour",
  "granola",
  "honey",
  "ice cream",
  "juice",
  "ketchup",
  "lemon",
  "margarine",
  "onion",
  "potatoes",
  "rosemary",
  "salt",
  "thyme",
  "vinegar",
  "watermelon",
  "pears",
  "cucumbers",
  "garlic",
  "carrots",
  "pastries",
  "eggplants",
  "milk",
  "coffee",
  "tea",
  "rice",
  "noodles",
  "lentils",
  "sweet potatoes",
  "strawberries",
  "cranberries",
  "mangos",
  "peppers",
  "zucchinis",
  "lime",
  "broth",
  "mushrooms",
  "chicken",
  "beef",
  "pork",
  "fish",
  "cream",
  "paprika",
  "tumeric",
  "cinnamon",
  "pumpkin",
  "basil",
  "tomatoes",
  "bread",
  "cake",
  "chocolate",
  "gum",
  "pineapple",
  "oranges",
  "lettuce",
  "cheese",
  "cilantro"
]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT )")
for i in range(len(groceries)):
    cursor.execute("insert into groceries (name) values (?)", [groceries[i]])
    print("added ", groceries[i])

connection.commit()
connection.close()
