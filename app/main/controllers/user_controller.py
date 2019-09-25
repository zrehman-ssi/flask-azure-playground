from flask_restful import Resource
from app.main.models.user import User
from app.main import db

class Hello(Resource):
    def get(self):
        user = User.query.filter_by(username='admin').first()
        if(user is not None):
            return user.email
        
        return "User not found"

    def post(self):
        admin = User(username='admin', email='admin@example.com')
        guest = User(username='guest', email='guest@example.com')
        db.session.add(admin)
        db.session.commit()
