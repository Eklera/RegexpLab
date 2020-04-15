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
    symbols = [".", "@", " "]





for line in txt:
    line = line.split("|")
    has_empty_elements = False
    for elem in line:
        if not elem:
            has_empty_elements = True
            break

    if len(line) != 4 or has_empty_elements:
        continue

    name, age, tel, mail = line






