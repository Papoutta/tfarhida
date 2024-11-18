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
        self.data=data["date"]
        self.password=data["password"]
        self.phone_number=data["phone_number"] 
        self.gender=data["gender"]
        self.photo=data["photo"] 
        self.role=data["role"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
    @classmethod  
    def register(cls,data): 
        qurey="INSERT INTO users (first_name,last_name,email,date,password,phone_number,gender,photo,role)VALUES (%(first_name)s, %(last_name)s, %(email)s,%(date)s, %(password)s, %(phone_number)s, %(gender)s,%(photo)s, %(role)s);"
        return connectToMySQL(DB).query_db(qurey,data)   
    ########################### 
    @classmethod 
    def get_by_email(cls,data):
        qurey="select * from users where email =%(email)s;"
        result=connectToMySQL(DB).query_db(qurey,data) 
        if result:
            return cls(result[0]) 
        return False   
    ########################
    @classmethod 
    def update(cls,data): 
        query="update user set first_name=%(first_name)s,last_name=%(last_name)s,date=%(date)s,date=%(date)s,phone_number=%(phone_number)s ,photo=%(photo)s, gender=%(gender)s where id=%(id)s;"
        result=connectToMySQL(DB).query_db(query,data) 
        return result
    ###########################
    @staticmethod
    def validate(data): 
        is_valide=True
        if len(data["first_name"])<2:
            flash("first name must be at least 2 characters","first_name")
            is_valide=False
        if len(data["last_name"])<2:
            flash("first name must be at least 2 characters","last_name")
            is_valide=False
        if not(EMAIL_REGEX.match(data["email"])):
            flash("email not valide","email") 
            is_valide=False  
        elif User.get_by_email({"email":data['email']}):
            flash ("email alread taken","email") 
            is_valide=False
        if (data["photo"]==""): 
            flash ("put photos","photo") 
            is_valide=False
        if len(data["password"])<7:
            flash("password must contain at least 7 charactes","password") 
        elif (data["password"]!=data["password_confirm"]): 
            flash("password don 't match","password_confirm") 
            is_valide=False
        return is_valide 


        