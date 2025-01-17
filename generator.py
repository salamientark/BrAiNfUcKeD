from typing import List
from io import TextIOWrapper

def open_file(file_name) :
    try :
        file = open(file_name, 'w')
        return file
    except :
        print("Error: File not found")
        return None

def generate_init(file: TextIOWrapper, var: List[str]) :
    for letter in var : # Save letter as brainfuck var
        file.write(ord(letter) * "+" + ">");
    file.write("<" * len(var))  # Goto begining
