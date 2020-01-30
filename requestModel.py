# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:StrongAdminP@ssw0rd@localhost:5432/nin"
# db = SQLAlchemy(app)

# class IssuedDateModel(db.Model):
#     tablename = "nin_slips"

#     id = db.Column(db.Integer, primary_key=True)
#     tracking_id = db.Column(db.String)
#     nin = db.Column(db.Integer)
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     middle_name = db.Column(db.String)
#     gender = db.Column(db.String)
#     issued_date = db.Column(db.Date)
#     age_category = db.Column(db.String)
    
#     def __init__(self, id, tracking_id, nin, first_name, last_name, middle_name, gender, issued_date, age_category):
#         self.tracking_id = tracking_id
#         self.nin = nin
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.gender = gender
#         self.issued_date = issued_date
#         self.age_category = age_category

#     def __repr__(self):
#         return f"(self.name)"
