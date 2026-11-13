import json
import os

class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.inventory = {}
        # Automatically load data when the library object is created
        self.load_data()

    def add_book(self, title, copies=1):
        if title in self.inventory:
            self.inventory[title] += copies
        else:
            self.inventory[title] = copies
        print(f"Added {copies} copy/copies of '{title}'.")
        # Save data immediately after modifying the inventory
        self.save_data()

    def list_books(self):
        print("\n--- Library Inventory ---")
        if not self.inventory:
            print("No books currently in the library.")
        else:
            for title, copies in self.inventory.items():
                print(f"'{title}': {copies} copies available")
        print("-------------------------\n")

    def save_data(self):
        # Writes the dictionary to a JSON file
        with open(self.filename, 'w') as file:
            json.dump(self.inventory, file, indent=4)
        print("Library data successfully saved to file.")

    def load_data(self):
        # Reads the dictionary from a JSON file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.inventory = json.load(file)
                    print(f"Library data loaded from '{self.filename}'.")
                except json.JSONDecodeError:
                    self.inventory = {}
        else:
            print("No existing data file found. Starting with an empty library.")
            self.inventory = {}

# --- SCRIPT EXECUTION ---

print("=== Initializing Library ===")
# This will load existing data if the script has been run before
my_library = Library()

# Show what is currently in the library
my_library.list_books()

print("=== Adding New Books ===")
my_library.add_book("The Pragmatic Programmer", 1)
my_library.add_book("Clean Code", 2)

# Show the updated library
my_library.list_books()
