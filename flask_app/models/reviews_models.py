from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash  
class Reviews: 
    def __init__(self,data) :  
        self.users_id=data["users_id"] 
        self.events_id=data["events_id"]  
        self.id=data["id"]  
        self.comment=data["comment"]  
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
    @classmethod 
    def reviews(cls,data): 
        qurey="insert into   reviews (comment,users_id,events_id) values ( %(comment)s,%(users_id)s,%(events_id)s);"
        print("*****************************************************************")
        print(qurey)
        return connectToMySQL(DB).query_db(qurey,data)  
    @classmethod
    def commente(cls,data): 
        qurey="select * from reviews  where events_id= %(events_id)s;" 
        results=connectToMySQL(DB).query_db(qurey,data)  
        # return results[0]
        all_comment=[]
        for row in results:
            all_comment.append(cls(row))
        return all_comment 
    
    
    