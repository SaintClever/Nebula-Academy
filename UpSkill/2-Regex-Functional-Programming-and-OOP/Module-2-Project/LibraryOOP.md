# 📚 Library Management System Project 📚

In this project, you will design a Library Management System using the power of Python 🐍 and Object-Oriented Programming (OOP). The system will simulate the workings of a basic library, where members can borrow and return books, and the library can add or remove books from its catalog.

## 🎯 Objectives 🎯

1. Apply your knowledge of Python and OOP principles.
2. Practice designing classes and creating objects.
3. Develop a functional Library Management System.

## 👨‍💻 Your Task 👩‍💻

Your Library Management System should involve the following classes and their respective functionality:

- **Book**: Each book should have a title, an author, and a status (available or borrowed).
- **Member**: Each member should have a name, a unique ID, and a list of currently borrowed books.
- **Library**: The library should maintain a catalog of books (a list of Book objects) and a list of members.

The system should allow for the following operations:

1. **Adding a book**: The library should be able to add books to its catalog.
2. **Removing a book**: The library should be able to remove books from its catalog.
3. **Borrowing a book**: Members should be able to borrow available books. When a book is borrowed, it should be marked as such and added to the member's list of borrowed books.
4. **Returning a book**: Members should be able to return borrowed books. When a book is returned, it should be marked as available and removed from the member's list of borrowed books.
5. **Displaying all books**: The library should be able to display all books in its catalog.
6. **Displaying all members**: The library should be able to display all its members.

## 📋 Rubric 📋

Here's what you should focus on while working on this project:

- **Class Design**: Have you appropriately designed your classes with the necessary attributes and methods? Are the relationships between classes correctly defined? 📐
- **Data Encapsulation**: Are you practicing proper data encapsulation with private attributes and public methods? 🛡️
- **Functionality**: Does your system correctly perform all required operations (add, remove, borrow, return, display)? 🏗️
- **Code Quality**: Is your code clean, well-structured, and easy to read? Are you following good naming conventions? Is your code properly documented with comments? 📖
- **Error Handling**: Does your system handle potential errors gracefully? For example, what happens if someone tries to borrow a book that's already borrowed? ⚠️

## 🏁 Submission 🏁

Submit a Python (.py) file containing your solution. Ensure your code is well-commented, so we can follow your thought process.

Good luck, and have fun building your Library Management System! 🚀👨‍💻👩‍💻

# Game Plan

Here's a step-by-step plan that can be used to guide the development of this project:

1. **Define the Book Class**:

   - Define the `__init__()` function to initialize `title`, `author`, and `status` attributes.
   - Define a `__str__()` method for a readable string representation of the Book object.

2. **Define the Member Class**:

   - Define the `__init__()` function to initialize `name`, `member_id`, and `borrowed_books` attributes.
   - Define methods for borrowing and returning a book.
   - Define a `__str__()` method for a readable string representation of the Member object.

3. **Define the Library Class**:

   - Define the `__init__()` function to initialize `catalog` and `members` attributes.
   - Define methods for adding and removing books, and registering members.
   - Define a `borrow_book()` method that allows a member to borrow a book if it is available.
   - Define a `return_book()` method that allows a member to return a book they've borrowed.
   - Define methods for displaying all books and members.

4. **Testing**: Create instances of the Book, Member, and Library classes to simulate the workings of a library. Test all methods to ensure they're working as expected.
