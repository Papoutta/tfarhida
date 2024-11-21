from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models import user_models,likes_models,reviews_models


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
        self.num_likes= likes_models.Like.number({"event_id":self.id})
        self.joined_users=Event.get_joined_users({"events_id": self.id})
        self.joined_users_with_names=Event.get_joined_users_with_names({"events_id": self.id})
        self.comment=reviews_models.Reviews.commente({"events_id":self.id}) 
        self.like_users=Event.get_like_users({"event_id": self.id})

        


    @classmethod
    def deny_status(cls, data):
        query="""
                UPDATE tfarhida_schema.groups SET status='Denied' 
                WHERE users_id = %(users_id)s AND events_id=%(events_id)s;
                """
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def accept_status(cls, data):
        query="""
                UPDATE tfarhida_schema.groups SET status='Accepted' 
                WHERE users_id = %(users_id)s AND events_id=%(events_id)s;
                """
        return connectToMySQL(DB).query_db(query,data)


    @classmethod
    def get_my_events(cls,data):
        query = "select * from events where users_id = %(users_id)s;"
        results=connectToMySQL(DB).query_db(query,data) 
        all_events=[]
        for row in results:
            all_events.append(cls(row))
        return all_events


    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO events (name, place, date, additional_information,photo,users_id,categories_id) values (%(name)s,%(place)s,%(date)s,%(additional_information)s,%(photo)s,%(users_id)s,%(categories_id)s); "
        return connectToMySQL(DB).query_db(query,data) 
    ##############################################################

    @classmethod
    def add_to_group(cls, data):
        query = "INSERT INTO tfarhida_schema.groups (users_id,events_id, status) values (%(users_id)s,%(events_id)s, 'Pending'); "
        return connectToMySQL(DB).query_db(query,data) 
    
    @classmethod
    def delete_from_group(cls, data):
        query = "DELETE FROM tfarhida_schema.groups WHERE users_id = %(users_id)s AND events_id=%(events_id)s; "
        return connectToMySQL(DB).query_db(query,data) 
        
    @classmethod
    def get_all_groups(cls,data):
        query="select *from tfarhida_schema.groups where users_id =%(users_id)s and events_id=%(events_id)s;"
        results=connectToMySQL(DB).query_db(query,data) 
        all_groups=[]
        for row in results:
            all_groups.append(cls(row))
        return all_groups

    @classmethod
    def get_user_events(cls,data):
        query="select * from events  where categories_id =%(categories_id)s;"
        results=connectToMySQL(DB).query_db(query,data) 
        all_events=[]
        for row in results:
            all_events.append(cls(row))
        return all_events
    
    @classmethod
    def get_all_events(cls):
        query="select * from events;"
        results=connectToMySQL(DB).query_db(query) 
        all_events=[]
        for row in results:
            all_events.append(cls(row))
        return all_events
    
    @classmethod
    def get_event_by_id(cls, data):
        query="select * from events where id = %(id)s;"
        results=connectToMySQL(DB).query_db(query,data) 
        return cls(results[0])
    
    @classmethod
    def get_joined_users(cls,data):
        query="""SELECT * FROM tfarhida_schema.groups

                    WHERE tfarhida_schema.groups.events_id = %(events_id)s;"""
        results=connectToMySQL(DB).query_db(query, data) 
        all_users=[]
        for row in results:
            all_users.append(row['users_id'])
        return all_users
    
    @classmethod
    def get_like_users(cls,data):
        query = """ select * from tfarhida_schema.likes
                where likes.event_id = %(event_id)s;
                    """
        results=connectToMySQL(DB).query_db(query, data) 
        all_users=[]
        for row in results:
            all_users.append(row['user_id'])
        return all_users

    @classmethod
    def get_joined_users_with_names(cls,data):
        query="""SELECT * FROM tfarhida_schema.groups
                JOIN users ON users.id= tfarhida_schema.groups.users_id
                    WHERE tfarhida_schema.groups.events_id = %(events_id)s;"""
        results=connectToMySQL(DB).query_db(query, data) 
        all_users=[]
        for row in results:
            all_users.append({'users_id':row['users_id'], 'username':row['first_name'], 'status': row['status']})
        return all_users
    
    @classmethod
    def get_accepted_users(cls, data):
        query="""
            SELECT * FROM tfarhida_schema.groups
                JOIN users ON users.id= tfarhida_schema.groups.users_id
                    WHERE tfarhida_schema.groups.events_id = %(id)s and tfarhida_schema.groups.status = "Accepted";
        """
        results=connectToMySQL(DB).query_db(query, data) 
        all_users=[]
        for row in results:
            all_users.append(row['users_id'])
        return all_users