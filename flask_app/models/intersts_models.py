from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash 
class Interests :
    def __init__(self,data):
        self.user_id=data["user_id"] 
        self.category_id=data["category_id"]
    @classmethod  
    def creat(cls,data):  
        qurey="insert into interests(user_id,category_id) values (%(user_id)s, %(category_id)s);" 
        result=connectToMySQL(DB).query_db(qurey,data)  
        return result 
    




