Books Model and Repository Classes Design Recipe
Copy this recipe template to design and implement Model and Repository classes for a database table.

1. Design and create the Table
If the table is already created in the database, you can skip this step.

Otherwise, follow this recipe to design and create the SQL schema for your table.

In this template, we'll use an example table students

Table: Books

Columns:
id | title | author_name

2. Create Test SQL seeds
Your tests will depend on data stored in PostgreSQL to run.

seeds/book_store.sql

3. Define the class names
Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

# Table name: books

# Model class
# (in lib/book.py)
Class Book:


# Repository class
# (in lib/book_repository.py)
Class BookRepository:

4. Implement the Model class
Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.


# Model class
# (in lib/book.py)

class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

5. Define the Repository Class interface
Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of book objects.


6. Write Test Examples
Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

# EXAMPLES

# 1
# Get all students

repo = BookRepository()

books = repo.all()

len(books) # =>  5

students[0].id # =>  1
students[0].title # =>  'Nineteen Eighty-Four'
students[0].cohort_name # =>  'George Orwell'

students[1].id # =>  2
students[1].name # =>  'Mrs Dalloway'
students[1].cohort_name # =>  'Virginia Woolf'

7. Test-drive and implement the Repository class behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

