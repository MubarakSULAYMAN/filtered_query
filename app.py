from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:StrongAdminP@ssw0rd@localhost:5432/nin"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://unuqhtroyxjkwp:322daedc54cc2a558437734eafc61a2ff75ed57814a0d597ae4d891fda59ce48@ec2-52-207-93-32.compute-1.amazonaws.com:5432/d8qirc81vetv7p"
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)



class RegisteredData(db.Model):
    __tablename__ = "nin_slips"

    id = db.Column(db.Integer, primary_key=True)
    tracking_id = db.Column(db.String(15), unique=True)
    nin = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    middle_name = db.Column(db.String(40))
    gender = db.Column(db.String(1))
    issued_date = db.Column(db.Date)
    age_category = db.Column(db.String(6))



@app.route('/restricted_raw', methods=['GET'])
def raw_request():
    query_term = RegisteredData.query.all()
    results = [
        {
            "tracking_id": table_data.tracking_id,
            "nin": table_data.nin,
            "first_name": table_data.first_name,
            "last_name": table_data.last_name,
            "middle_name": table_data.middle_name,
            "gender": table_data.gender,
            "issued_date": table_data.issued_date,
            "age_category": table_data.age_category
        }
        for table_data in query_term
    ]    

    JSONObjects = {"count": len(results), "query_term": results}
    return jsonify(JSONObjects), 200



@app.route('/filter_by_nin/<nin>', methods=['GET'])
def nin_request(nin):
    query_term = RegisteredData.query.filter_by(nin=nin).all()
    results = [
        {
            "tracking_id": table_data.tracking_id,
            "nin": table_data.nin,
            "first_name": table_data.first_name,
            "last_name": table_data.last_name,
            "middle_name": table_data.middle_name,
            "gender": table_data.gender,
            "issued_date": table_data.issued_date,
            "age_category": table_data.age_category
        }
        for table_data in query_term
    ]    

    JSONObjects = {"count": len(results), "query_term": results}
    return jsonify(JSONObjects), 200



@app.route('/filter_by_tracking_id/<tracking_id>', methods=['GET'])
def last_name_request(tracking_id):
    query_term = RegisteredData.query.filter_by(tracking_id=tracking_id).all()
    results = [
        {
            "tracking_id": table_data.tracking_id,
            "nin": table_data.nin,
            "first_name": table_data.first_name,
            "last_name": table_data.last_name,
            "middle_name": table_data.middle_name,
            "gender": table_data.gender,
            "issued_date": table_data.issued_date,
            "age_category": table_data.age_category
        }
        for table_data in query_term
    ]    

    JSONObjects = {"count": len(results), "query_term": results}
    return jsonify(JSONObjects), 200



@app.route('/filter_by_issued_date/<issued_date>', methods=['GET'])
def issued_date_request(issued_date):
    query_term = RegisteredData.query.filter_by(issued_date=issued_date).all()
    results = [
        {
            "tracking_id": table_data.tracking_id, 
            "nin": table_data.nin,
            "first_name": table_data.first_name,
            "last_name": table_data.last_name,
            "middle_name": table_data.middle_name,
            "gender": table_data.gender,
            "issued_date": table_data.issued_date,
            "age_category": table_data.age_category
        }
        for table_data in query_term
    ]    

    JSONObjects = {
        "count": len(results), 
        "query_term": results,
        "mimetype": application/json},
    return jsonify(JSONObjects), 200



# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
