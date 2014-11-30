from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


#{'root': {'active': True, 
# 'apikey': None, 
# 'password': 'ca32cd0874d8047c2298b5ac16d89ce71423fdbad407c67aff753278c7d5319ffe8ecac01a1a0d2c4da92762c4798b8fbbc7e178357d3c6cadc60531e55c5070', 
# 'roles': ['admin', 'user']}}

#Octoprint User Class
class DBUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    active = db.Column(db.String(10))
    apikey = db.Column(db.String(256))
    password = db.Column(db.String(256))

    def __init__(self, username, active='False', apikey='None', password='None'):
        self.username = username
        self.active = active
        self.apikey = apikey
        self.password = password

    def __repr__(self):
        return '{\'%s\': {\'active\': %s, \'apikey\': %s, \'password\': \'%s\', \'roles\': [\'admin\', \'user\'] }}' % (self.username, self.active, self.apikey, self.password)

#Octoprint Role Class
# One to many relationship from Users to roles
# class Role(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userid = db.Column(db.Integer, db.ForeignKey('user.id'))
#     role = db.Column(db.String(10))

#     def __init__(self, role):
#         self.role = role

#     def __repr__(self):
#         return '<Role %r>' % self.role        