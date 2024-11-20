from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash  
class Like: 
    def __init__(self,data) :  
        self.user_id=data["user_id"] 
        self.event_id=data["event_id"] 
    @classmethod
    def likes(cls,data): 
        qurey="insert into likes (user_id,event_id)values (%(user_id)s,%(event_id)s);"
        return connectToMySQL(DB).query_db(qurey,data) 
    @classmethod
    def number(cls,data):
        query="select count(*) as like_count from likes  where event_id= %(event_id)s;"
        rsult=connectToMySQL(DB).query_db(query,data) 
        return rsult[0]   
    @classmethod
    def delte(cls,data):
        qurey="delete from likes where user_id=%(user_id)s and event_id=%(event_id)s;"  
        rsult=connectToMySQL(DB).query_db(qurey,data)
        return rsult 
    
        
