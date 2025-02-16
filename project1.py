"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
discord: ledvinaj
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#uživatelé a jejich hesla
users = {
 "bob": "123",
 "ann": "pass123",
 "mike": "password123",
 "liz": "pass123"
} 
separator = "-" * 50

#přihlášení uživatele do aplikace
username = input("Enter username: ")
password = input("Enter password: ")
print(separator)

#ověření uživatele
if  users.get(username) == password:
    print(f"Welcome to the app, {username}")
    
else:
  print(username)
  print(password)
  print("eunregistred user, terminatng the program..")
  exit()

#ANALÝZA TEXTU
#výběr čísla textu pro analýzu
print("We have 3 texts to be analyzed")
print(separator)
select_user = int(input("Enter a number btw. 1 and 3 to select: "))
print(separator)

#analýza textu vybraného uživatelem
if select_user == 1 or select_user == 2 or select_user == 3:
  #přiřazení konkrétního textu do proměné
  select_text = TEXTS[(select_user) - 1]

  #rozdělení textu na slova
  words = select_text.split()
  print(f"There are {len(words)} words in the selected text.")

#počet slov s začínající velkým písmenem v textu
  capital_words = []
  for word in words:
    if word.istitle():
      capital_words.append(word)
  print(f"There are {len(capital_words)} titlecase words.")

#počet slov psaný velkými písmeny s podmínkou vynechat slova s číslem
  uppercase_words = []
  for word in words:
    if word.isupper() and not word.isalpha():
      uppercase_words.append(word)
  print(f"There are {len(uppercase_words)} uppercase words.")


#počet slov psaný malými písmeny
  lower_words = []
  for word in words:
    if word.islower():
      lower_words.append(word)
  print(f"There are {len(lower_words)} lowercase words.")

#počet čísel (ne cifer)
  numbers = []
  for word in words:
    if word.isnumeric():
      numbers.append(word)
  print(f"There are {len(numbers)} numeric strings.")

#suma všech čísel
  suma = []
  for number in words:
    if number in numbers:
      suma.append(int(number))
  print(f"The sum of all the numbers {sum(suma)}.")
 


else:
  print("The number does't exist. terminatng the program..")
  exit()

#graf analýzy

#halvička grafu 
print(separator)
print(f"{'LEN':2}| {'OCCURENCES':17} |NR.")
print(separator)


#zjištění délky slov a odstranení znaků
word_lenghts = []
for word in words:
  word_lenghts.append(len(word.strip(",.?!")))
#print(word_lenghts)

#seřazení slov a odstranění opakujících se slov
words_list = sorted(set(word_lenghts))
#print(words_list)

#cykl na vypsání konečného grafu
for lenght in words_list:
  count = word_lenghts.count(lenght)
  characters = "*" * count
  #výstup s rormátování textu
  print(f"{lenght:2} | {characters:17} |{count}")


