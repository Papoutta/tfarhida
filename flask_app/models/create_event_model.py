from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models.category_model import Category

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.name = data['name']
        self.place = data['place']
        self.date = data['date']
        self.additional_informtaion = data['additional_informtaion']  
        self.photo = data['photo']


    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO events (type, name, place, date, additional_information,photo) values (%(type)s,%(name)s,%(place)s,%(date)s,%(additional_information)s,%(photo)s) "
        return connectToMySQL(DB).query_db(query,data) 
    ############################################################## 
  
  

    

        