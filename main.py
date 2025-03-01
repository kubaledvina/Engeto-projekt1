"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
discord: ledvinaj
"""

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
  print("unregistered user, terminating the program..")
  exit()

#ANALÝZA TEXTU
#výběr čísla textu pro analýzu
print("We have 3 texts to be analyzed")
print(separator)
selected_text = int(input("Enter a number btw. 1 and 3 to select: "))
print(separator)
  
#analýza textu vybraného uživatelem
if selected_text in [1, 2, 3]:
  #přiřazení konkrétního textu do proměné
  selected_index_text = TEXTS[(selected_text) - 1]
else:
  print("The number does't exist. terminating the program..")
  exit()
 
#rozdělení textu na slova
words = selected_index_text.split()

#celkový počet slov v textu
print(f"There are {len(words)} words in the selected text.")

#počet slov s začínající velkým písmenem v textu
capital_words = [word for word in words if word.istitle()]  
print(f"There are {len(capital_words)} titlecase words.")

#počet slov psaný velkými písmeny s podmínkou vynechat slova s číslem
uppercase_words = [word for word in words if word.isupper()]
print(f"There are {len(uppercase_words)} uppercase words.")

#počet slov psaný malými písmeny 
lower_words = [word for word in words if word.islower()]
print(f"There are {len(lower_words)} lowercase words.")

#počet čísel (ne cifer)
numbers_in_text = [number for number in words if number.isdigit()]
print(f"There are {len(numbers_in_text)} numeric strings.")

#suma všech čísel
suma_numbers = sum(int(number) for number in numbers_in_text)
print(f"The sum of all the numbers {suma_numbers}.")

#graf analýzy
#halvička grafu 
print(separator)
print(f"{'LEN':2}| {'OCCURENCES':17} |NR.")
print(separator)

#zjištění délky slov a odstranení znaků
word_lenghts = [len(word.strip(",.?!")) for word in words]

#slovník pro počítání délky slov
words_counter = {lenght: word_lenghts.count(lenght) for lenght in sorted(set(word_lenghts))}

#cykl na vypsání konečného grafu
for lenght, count in words_counter.items():
  print(f"{lenght:2} | {'*' * count:17} |{count}")


