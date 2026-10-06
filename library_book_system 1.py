# Test output:
# 978-0441013593    Dune                     Frank Herbert          1965 Science Fiction    Available
# Checkout: True; available=False; borrower=Jordan
# Second checkout: False; borrower=Jordan
# 'Dune' has been returned and is now available.
# After return: available=True; borrower=None
# Sorted: 1984, Dune, Educated
# Original: Dune, 1984, Educated
# Available after checkout: 1984, Educated
# Main program: 6 books displayed; 5 available after loans and return.

# Week 6: Library Book Management System
# Assignment level: Base


class Book:
    # Store the book details and mark it available.
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    # Return the book details and loan status in columns.
    def __str__(self):
        return (
            f"{self.isbn:<17} {self.title:<24} {self.author:<22} "
            f"{self.year:>4} {self.genre:<18} {self.get_status()}"
        )

    # Reject a second checkout without replacing the borrower.
    def check_out(self, patron_name):
        if not self.available:
            return False
        self.available = False
        self.borrower = patron_name
        return True

    # Clear the loan when the book is returned.
    def return_book(self):
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    # Return the current loan status.
    def get_status(self):
        if self.available:
            return "Available"
        return f"Checked out to {self.borrower}"


# Show the required operations using six books.
def main():
    collection = [
        Book("Dune", "Frank Herbert", "978-0441013593",
             1965, "Science Fiction"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565",
             1925, "Classic Fiction"),
        Book("Educated", "Tara Westover", "978-0399590504",
             2018, "Memoir"),
        Book("The Hobbit", "J. R. R. Tolkien", "978-0547928227",
             1937, "Fantasy"),
        Book("1984", "George Orwell", "978-0451524935",
             1949, "Dystopian Fiction"),
        Book("Pride and Prejudice", "Jane Austen", "978-0141439518",
             1813, "Classic Fiction"),
    ]

    print("=== Full Collection ===")
    for item in collection:
        print(item)

    print("\n=== Checkouts ===")
    borrowers = ["Jordan", "Priya"]
    for index in range(2):
        item = collection[index]
        reader = borrowers[index]
        if item.check_out(reader):
            print(f"'{item.title}' checked out to {reader}.")
        else:
            print(f"'{item.title}' is already checked out.")

    # Dune is already on loan to Jordan.
    if collection[0].check_out("Alex"):
        print(f"'{collection[0].title}' checked out to Alex.")
    else:
        print(f"'{collection[0].title}' is already checked out.")

    print("\n=== Return ===")
    print(collection[1].return_book())

    print("\n=== Collection Sorted by Title ===")
    for item in sorted(collection, key=lambda entry: entry.title):
        print(item)

    print("\n=== Available Books ===")
    on_shelf = [item for item in collection if item.available]
    for item in on_shelf:
        print(item)


if __name__ == "__main__":
    main()
