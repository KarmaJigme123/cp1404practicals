"""
CP1404: Practical 1
Student name: Karma Jigme Wangchuk
Program: Menus
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print("Goodbye")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print('Finished')