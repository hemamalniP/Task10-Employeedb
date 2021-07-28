from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class empfam(db.Model):
    __tablename__='empfamily'
    place = db.Column(db.String(100))
    pincode = db.Column('pincode', db.Integer, primary_key=True)
    def __init__(self,place,pincode):
        self.place=place
        self.pincode=pincode
db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
