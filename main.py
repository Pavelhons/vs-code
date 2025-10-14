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
#registrovaní uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
#přihlášení
username = input("username: ")
password = input("password: ")
print("----------------------------------------")
if username in users and users[username] == password:
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")
else:
    print("unregistered user, terminating the program..")
    quit()
   

#výběr zvoleného textu
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if not choice.isdigit() or not (1 <= int(choice) <= len(TEXTS)):
    print("Invalid selection, terminating the program..")
    quit()
text = TEXTS[int(choice) - 1]

#analýza textu

words = [word.strip(",.!?") for word in text.split()]

word_count = len(words)
titlecase_count = sum(1 for w in words if w.istitle())
uppercase_count = sum(1 for w in words if w.isupper() and w.isalpha())
lowercase_count = sum(1 for w in words if w.islower())
numeric_count = sum(1 for w in words if w.isdigit())
sum_numbers = sum(int(w) for w in words if w.isdigit())

#výsledky
print("----------------------------------------")
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}.")
print("----------------------------------------")

#graf délky slov
lengths = {}
for word in words:
    length = len(word)
    lengths[length] = lengths.get(length, 0) + 1

# seřazení podle délky slova
print("LEN| OCCURENCES |NR.")
print("----------------------------------------")
for length in sorted(lengths):
    print(f"{length:>3}| {'*' * lengths[length]} {lengths[length]}")
