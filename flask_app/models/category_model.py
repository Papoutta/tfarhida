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
    
    @classmethod
    def get_by_category(cls, data):
        query = "SELECT *FROM categories WHERE category_name = %(category_name)s;"
        result = connectToMySQL(DB).query_db(query , data)
        if result :
            return cls(result[0])
        return False


    @classmethod 
    def intersts(cls,data):
        query="SELECT * FROM categories WHERE categories.id NOT IN ( SELECT category_id FROM interests WHERE interests.user_id = %(user_id)s );"
        result=connectToMySQL(DB).query_db(query,data) 
        all_categories=[]
        for row in result:
            all_categories.append(cls(row))
        return all_categories
    
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['category_name'])<3:
            is_valid=False
            flash(" Category name is too short", 'category_name')
        elif Category.get_by_category({"category_name": data['category_name']}):
            flash("category already taken", "category_name")
            is_valid = False
        return is_valid 
    # @staticmethod