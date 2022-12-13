import json
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
CORS(app)
db = SQLAlchemy(app)

# model
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


# views
@app.route('/students/', methods = ["GET", 'POST',"DELETE","PUT"])
@app.route('/students/<id>', methods = ["GET", 'POST',"DELETE","PUT"])
def students_aaa(id=-1):
    if request.method =="GET": # read
        if id > -1: #single
            student = students.query.get(id)    
            return({"addr":student.addr,"city":student.city,"id":student.id,"name":student.name,"pin":student.pin})
        else: #many
            res=[]
            for student in students.query.all():
                res.append({"addr":student.addr,"city":student.city,"id":student.id,"name":student.name,"pin":student.pin})
            return  (json.dumps(res))
    if request.method =="POST": # Create
        request_data = request.get_json()
        # print(request_data['city'])
        city = request_data['city']
        name= request_data["name"]
        addr= request_data["addr"]
        pin= request_data["pin"]
    
        newStudent= students(name,city,addr,pin)
        db.session.add (newStudent)
        db.session.commit()
        return "a new record was create"
    if request.method =="DELETE": #delete
        print(id)
        me = students.query.get(id)
        if(me):
            db.session.delete(me)
            db.session.commit()
            return "delete"
        else:
            return "unknown id"
    if request.method =="PUT":
        me = students.query.get(id)
        request_data = request.get_json()
        me.city = request_data['city']
        me.name= request_data["name"]
        me.addr= request_data["addr"]
        me.pin= request_data["pin"]
        db.session.commit()
        return "a row was update" #Update

if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug = True)


