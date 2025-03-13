import json
import os

def load_data():
    with open("archief.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("archief.json", "w") as file:
        json.dump(data, file)

def add_entry():
    name = input("Enter name: ")
    description = input("Enter description: ")
    data = load_data()
    data.append({"name": name, "description": description})
    save_data(data)

def view_entries():
    data = load_data()
    for entry in data:
        print(f"{entry['name']}: {entry['description']}")

def menu():
    while True:
        print("1. View Entries")
        print("2. Add Entry")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            view_entries()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            break
        else: 
            print("helaas is dat niet een van de nummers.")
            

menu()
