from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:user10@localhost:5432/empdb'
app.debug=True
db = SQLAlchemy(app)
class empdet(db.Model):
    __tablename__='empdetail'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(50))
    place = db.Column(db.String(200))
    pincode = db.Column(db.String(50))
    doj = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    salary = db.Column(db.String(200))
    def __init__(self,id,name,age,place,pincode,doj,contact,salary):
        self.id = id
        self.name = name
        self.age = age
        self.place = place
        self.pincode = pincode
        self.doj = doj
        self.contact = contact
        self.salary = salary
@app.route('/emp',methods=['POST'])
def emrec():
    id = request.args.get('id')
    name = request.args.get('name')
    age = request.args.get('age')
    place = request.args.get('place')
    pincode = request.args.get('pincode')
    doj = request.args.get('salary')
    contact = request.args.get('contact')
    salary = request.args.get('salary')
    ipt = request.get_json()
    print(ipt)
    det = empdet(id=ipt['id'],name=ipt['name'],age=ipt['age'],place=ipt['place'],pincode=ipt['pincode'],doj=ipt['doj'],contact=ipt['contact'],salary=ipt['salary'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")
if __name__ == '__main__':
    app.run(debug=True)