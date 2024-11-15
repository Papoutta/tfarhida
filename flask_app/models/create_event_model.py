from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.name = data['name']
        self.place = data['place']
        self.time = data['time']
        self.additional_informtaion = data['additional_informtaion']
    
    @classmethod
    def save(data):
        query = "INSERT INTO events (type, name, place, time, additional_informtaion) values (%(type)s,%(name)s,%(place)s,%(time)s,%(additional_informtaion)s) "
        return connectToMySQL(DB).query_db(query,data)
    
    

        