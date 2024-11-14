from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash

class Category :
    def __init__(self, data):
        self.id=data["id"]
        self.category_name=data["category_name"]

    @classmethod
    def create(cls,data):
        query = """INSERT INTO categories
                    (category_name)
                    VALUES (%(category_name)s);
                """
        return connectToMySQL(DB).query_db(query,data)
    

    @classmethod
    def get_all(cls):
        query="SELECT * FROM categories;"
        results=connectToMySQL(DB).query_db(query)
        all_categories=[]
        for row in results:
            all_categories.append(cls(row))
        return all_categories