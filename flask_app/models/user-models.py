from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User: 
    def __init__(self,data): 
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.phone_number=data["phone_number"]
        self.created_at=data["created_at"]
        self.uqdated_at=data["uqdated_at"]
    @classmethod 
    def register(cls,data): 
        qurey="insert into users(first_name,last_name,email,password)values(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DB).query_db(qurey,data) 