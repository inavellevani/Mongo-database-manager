from pymongo import MongoClient


class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client[db_name]

    def add_data(self, table_name, **kwargs):
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        result = self.database["student_advisor"].find()
        return [(i["student_id"], i["advisor_id"]) for i in result]

    def delete_row(self, table_name, row_id):
        if table_name == "advisors":
            self.database[table_name].delete_one({"advisor_id": row_id})
        if table_name == "students":
            self.database[table_name].delete_one({"student_id": row_id})

    def load_data(self, table_name):
        return list(self.database[table_name].find({}, {"_id": 0}))

    def search(self, table_name, name=None, age=None, surname=None, student_id=None, advisor_id=None):
        query = {}
        if student_id:
            query["student_id"] = student_id
        if advisor_id:
            query["advisor_id"] = advisor_id
        if name:
            query["name"] = {"$regex": f".*{name}.*"}
        if surname:
            query["surname"] = {"$regex": f".*{surname}.*"}
        if age:
            query["age"] = {"$regex": f".*{age}.*"}

        return list(self.database[table_name].find(query, {"_id": 0}))

    def update(self, table_name, name, surname, age, id):
        query = {"student_id": id} if table_name == "students" else {"advisor_id": id}
        new_values = {"$set": {"name": name, "surname": surname, "age": age}}
        self.database[table_name].update_one(query, new_values)

    def check_bd(self):
        count = self.database["student_advisor"].count_documents({})
        if count == 0:
            print("No student-advisors found")
        else:
            print("Data available")

    def list_advisors_with_students_count(self, order_by):
        pipeline = [
            {"$lookup": {
                "from": "student_advisor",
                "localField": "advisor_id",
                "foreignField": "advisor_id",
                "as": "students"
            }},
            {"$project": {
                "advisor_id": 1,
                "name": 1,
                "surname": 1,
                "student_count": {"$size": "$students.student_id"}
            }},
            {"$sort": {"student_count": order_by}}
        ]
        return list(self.database["advisors"].aggregate(pipeline))

    def list_students_with_advisors_count(self, order_by):
        pipeline = [
            {"$lookup": {
                "from": "student_advisor",
                "localField": "student_id",
                "foreignField": "student_id",
                "as": "advisors"
            }},
            {"$project": {
                "student_id": 1,
                "name": 1,
                "surname": 1,
                "advisor_count": {"$size": "$advisors.advisor_id"}
            }},
            {"$sort": {"advisor_count": order_by}}
        ]
        return list(self.database["students"].aggregate(pipeline))
