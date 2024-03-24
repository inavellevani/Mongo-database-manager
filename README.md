This Python project provides a class DatabaseManager that allows you to interact with a MongoDB database using PyMongo. The class offers a range of methods to perform various operations, such as creating, reading, updating, and deleting data, as well as advanced querying and aggregation.

To get started, make sure you have Python and MongoDB installed on your system. Then, install the required Python package by running pip install pymongo. Import the DatabaseManager class from the project file, and create an instance by providing the database name: db_manager = DatabaseManager("my_database").

The DatabaseManager class includes the following methods:

add_data(table_name, **kwargs): Insert a new document into the specified collection (table) using keyword arguments. For example, db_manager.add_data("students", student_id=1, name="John", surname="Doe", age=25) will add a new student document to the "students" collection.

get_existing_relations(): Retrieve a list of tuples containing student-advisor relationships from the "student_advisor" collection.

delete_row(table_name, row_id): Delete a document from the specified collection based on the provided row ID. For example, db_manager.delete_row("students", 1) will delete the student document with the student_id of 1.

load_data(table_name): Retrieve all documents from the specified collection, excluding the "_id" field.

search(table_name, name=None, age=None, surname=None, student_id=None, advisor_id=None): Search for documents in the specified collection based on provided criteria. You can pass one or more of the provided parameters to filter the search results.

update(table_name, name, surname, age, id): Update the name, surname, and age fields of a document in the specified collection based on the provided ID.

check_bd(): Check if there are any existing student-advisor relationships in the "student_advisor" collection and print an appropriate message.

list_advisors_with_students_count(order_by): Retrieve a list of advisors with the count of their associated students, sorted in the specified order (1 for ascending, -1 for descending).

list_students_with_advisors_count(order_by): Retrieve a list of students with the count of their associated advisors, sorted in the specified order (1 for ascending, -1 for descending).

You can use these methods to perform various operations on your MongoDB database. For example, students = db_manager.search("students", name="John") will retrieve a list of student documents where the name field contains "John". db_manager.update("students", name="John", surname="Smith", age=26, id=1) will update the student document with the ID of 1, setting the name to "John", surname to "Smith", and age to 26.

This project assumes the existence of three collections in the MongoDB database: "advisors", "students", and "student_advisor". The "advisors" and "students" collections store information about advisors and students, respectively, while the "student_advisor" collection stores the relationships between students and their advisors.
