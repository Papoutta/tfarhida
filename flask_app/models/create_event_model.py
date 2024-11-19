from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models.category_model import Category

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.place = data['place']
        self.date = data['date']
        self.additional_informtaion = data['additional_informtaion']  
        self.photo = data['photo']
        self.users_id = data['users_id']
        self.categories_id = data['categories_id']


    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO events (name, place, date, additional_information,users_id,categories_id) values (%(name)s,%(place)s,%(date)s,%(additional_information)s,%(users_id)s,%(categories_id)s); "
        return connectToMySQL(DB).query_db(query,data) 
    ##############################################################
    

    

        