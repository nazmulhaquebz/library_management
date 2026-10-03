# Q4 - Weekly Borrowing Statistics

# Given list: books borrowed per week (Week 1 through Week 7)
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original list:", borrowed_books)

# a. Extract Week 2 to Week 5 using slicing (index 1 to 4 inclusive)
week_2_to_5 = borrowed_books[1:5]
print("Sliced (Week 2 to Week 5):", week_2_to_5)

# b. Replace Week 1 value (index 0) with 20 using indexing
borrowed_books[0] = 20
print("After replacing Week 1 with 20:", borrowed_books)

# c. Display updated list and sliced portion
print("\n--- Summary ---")
print("Updated weekly statistics:", borrowed_books)
print("Week 2 to Week 5 borrowings:", week_2_to_5)