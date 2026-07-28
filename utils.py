import os

def clear():
    os.system("cls")


def text(*text):
    print("\n" + "=" * 60 )
    print("\n", text[0].center(60))
    print("\n",*text[1:])