from langdetect import detect

with open('translate', encoding="utf8") as trans:
    content = trans.readlines()
print(content)

print(detect('Hello how are you'))

def translate():
    str = input("Enter text: ")
    while len(str) is 0:
        str = input("Enter text: ")
    if detect(str) is "ch":
        print("It's chinese")
    if detect(str) is "en":
        print("It's english")
    else:
        print(str)

translate()