# Q1 - Library Book List Management

# a. Create initial book list
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Initial list:", books)

# b. Add two more books using append()
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")
print("After adding books:", books)

# c. Remove a damaged book using remove()
books.remove("Moby Dick")
print("After removing damaged book:", books)

# d. Sort alphabetically and display
books.sort()
print("Final sorted list:", books)