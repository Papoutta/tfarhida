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
        self.date=data["date"]
        self.password=data["password"]
        self.phone_number=data["phone_number"] 
        self.gender=data["gender"]
        self.photo=data["photo"] 
        self.role=data["role"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.interests = User.get_interets({"user_id": self.id})
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
        query="update users set first_name=%(first_name)s,last_name=%(last_name)s,date=%(date)s,phone_number=%(phone_number)s , gender=%(gender)s where id=%(id)s;"
        result=connectToMySQL(DB).query_db(query,data) 
        return result
    ########################### 
    @classmethod 
    def get_user(cls,data):
        query="select *from users  where id =%(id)s;"
        result=connectToMySQL(DB).query_db(query,data) 
        if result:
            return cls(result[0]) 
        return False  
    
    @classmethod
    def get_interets(cls, data):
        query=""" SELECT * FROM tfarhida_schema.interests
                    join  categories on categories.id = interests.category_id
                    WHERE tfarhida_schema.interests.user_id = %(user_id)s;"""
        results=connectToMySQL(DB).query_db(query, data) 
        all_categories=[]
        for row in results:
            all_categories.append({'category_id':row['category_id'], 'category_name' :row['category_name']})
        return all_categories
    

    @classmethod
    def get_interests_names(cls,data):
        query = """SELECT category_name FROM tfarhida_schema.interests 
        join categories on categories.id = interests.category_id 
        where user_id = %(user_id)s;"""
        results=connectToMySQL(DB).query_db(query,data) 
        all_intersts=[]
        for row in results:
            all_intersts.append(cls(row))
        return all_intersts

    ###########################
    @staticmethod
    def validate(data: dict): 
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
        if "photo" in data.keys() and data["photo"]=="": 
            flash ("put photos","photo") 
            is_valide=False
        if  "password" in data.keys() and len(data["password"])<7:
            flash("password must contain at least 7 charactes","password") 
        elif "password_confirm" in data.keys()and  (data["password"]!=data["password_confirm"]): 
            flash("password don 't match","password_confirm") 
            is_valide=False
        return is_valide 


        