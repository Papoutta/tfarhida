from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models import user_models

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.place = data['place']
        self.date = data['date']
        self.additional_information = data['additional_information']  
        self.photo = data['photo']
        self.users_id = data['users_id']
        self.categories_id = data['categories_id']
        self.poster = user_models.User.get_user({"id":self.users_id})


    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO events (name, place, date, additional_information,photo,users_id,categories_id) values (%(name)s,%(place)s,%(date)s,%(additional_information)s,%(photo)s,%(users_id)s,%(categories_id)s); "
        return connectToMySQL(DB).query_db(query,data) 
    ##############################################################

    @classmethod
    def add_to_group(cls, data):
        query = "INSERT INTO tfarhida_schema.groups (users_id,events_id) values (%(users_id)s,%(events_id)s); "
        return connectToMySQL(DB).query_db(query,data) 
    
    @classmethod
    def delete_from_group(cls, data):
        query = "DELETE FROM tfarhida_schema.groups WHERE users_id = %(users_id)s AND events_id=%(events_id)s; "
        return connectToMySQL(DB).query_db(query,data) 
    @classmethod
    def get_user_events(cls,data):
        query="select *from events  where users_id =%(users_id)s;"
        results=connectToMySQL(DB).query_db(query,data) 
        all_events=[]
        for row in results:
            all_events.append(cls(row))
        return all_events