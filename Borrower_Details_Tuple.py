# Q2 - Borrower Details Tuple

# a. Create borrower tuple
borrower = ("John Doe", "B1023", "2025-10-15")
print("Borrower details:", borrower)

# b. Attempt to modify one element
try:
    borrower[0] = "Jane Doe"
except TypeError as e:
    print("Modification error:", e)

# c. Print length and display each element using a loop
print("Number of data fields:", len(borrower))
labels = ["Name", "Library ID", "Membership Date"]
for label, value in zip(labels, borrower):
    print(f"  {label}: {value}")