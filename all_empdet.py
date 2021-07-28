from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc,desc,func
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
class empfam(db.Model):
    __tablename__='empfamily'
    id = db.Column('id', db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100))
    father_name = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    marital_status = db.Column(db.String(50))
    def __init__(self,id,emp_name,father_name,mother_name,marital_status):
        self.id=id
        self.emp_name=emp_name
        self.father_name=father_name
        self.mother_name=mother_name
        self.marital_status=marital_status

@app.route('/all',methods=['GET'])
def all():
    det = db.session.query(empdet).join(empfam, empfam.id == empdet.id).filter(empdet.place =="RT nagar").with_entities(empdet.id,empfam.emp_name,empfam.father_name,empfam.mother_name,empfam.marital_status).limit(10).all()
    res = []
    for row in det:
        row_as_dict = dict(row)
        res.append(row_as_dict)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)