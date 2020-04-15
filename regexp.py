# Author: Valeriya Timofeeva
import re

txt = ""
with open("text.txt", "r", encoding='utf-8') as f:
    # noinspection PyRedeclaration
    txt = f.readlines()


if not txt:
    print("File is empty")
    exit()

name_pattern = re.compile(r"^([А-Я][а-я]*){2,3}")
age_pattern = re.compile(r"\d+")
tel_pattern = re.compile(r"\+{0,1}\d{11}")
mail_pattern = re.compile(r"[\w!#$%&'*+-/=?^_`{|]+[^.@]@(\w+.)+\w+")


def error_symbols(arg):
    arg = re.sub(r"\.+", ".", arg)
    arg = re.sub(r"@+", "@", arg)
    arg = re.sub(r" ", "", arg)
    return arg


for line in txt:
    line = line.strip()
    print(line)
    line = line.split("|")
    has_empty_elements = False
    for elem in line:
        if not elem:
            has_empty_elements = True
            break

    if len(line) != 4 or has_empty_elements:
        continue

    name, age, tel, mail = line

    name = error_symbols(name)
    age = error_symbols(age)
    tel = error_symbols(tel)
    mail = error_symbols(mail)

    name = re.search(name_pattern, name)
    age = re.search(age_pattern, age)
    tel = re.search(tel_pattern, tel)
    mail = re.search(mail_pattern, mail)

    if name is not None:
        print(name.group(0), end="|")
    else:
        print("Invalid name", end="|")

    if age is not None:
        print(age.group(0), end="|")
    else:
        print("Invalid age", end="|")

    if tel is not None:
        print(tel.group(0), end="|")
    else:
        print("Invalid tel", end="|")

    if mail is not None:
        print(mail.group(0))
    else:
        print("Invalid mail")
    print()




