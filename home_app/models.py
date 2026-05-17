from app.db import DATABASE
import flask_login as flask_login


class User(DATABASE.Model, flask_login.UserMixin):
    
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    email = DATABASE.Column(DATABASE.String)
    password_hash = DATABASE.Column(DATABASE.String)
    
    laptop = DATABASE.relationship("Laptop", back_populates="user", uselist = False)
    

class Laptop(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    color = DATABASE.Column(DATABASE.String)
    
    
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('user.id'))
    user = DATABASE.relationship("User", back_populates="laptop")


class UserGroup(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer,primary_key = True )
    
    # Указываем поля в которых записаны ссылки на записи, которые связаны
    user_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey("user.id"))
    group_id = DATABASE.Column(DATABASE.Integer, DATABASE.ForeignKey('group.id'))
    

# 
class Group(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    group_name = DATABASE.Column(DATABASE.String)
    
    

# 
class Message():
    pass

