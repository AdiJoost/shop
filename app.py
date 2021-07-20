import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
#import create_table
from resources.item import Item, Item_list
from resources.store import Store, Stores
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oypgvdlzwrpazt:8696cb28f37459857e4e7105fddf18a840fb4ebe65ae460eae53a101ebcd8143@ec2-54-74-77-126.eu-west-1.compute.amazonaws.com:5432/d6v6vhhsp2f6ik'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "LolHAHAHA"
api = Api(app)

jwt = JWT(app, authenticate, identity)

#create_table.create_table()

def get_db_url():
    uri = os.environ.get('DATABASE_URL')
    uri_cut = uri[8:]
    return "postgresql{}".format(uri_cut)    

@app.before_first_request
def create_table():
    db.create_all()

           
    
    
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_list, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, host="0.0.0.0", debug=True)
