from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# import requestModel
# import dbconnect

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:StrongAdminP@ssw0rd@localhost:5432/nin"
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)



class IssuedDateModel(db.Model):
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
    
    # def __init__(self, id, tracking_id, nin, first_name, last_name, middle_name, gender, issued_date, age_category):
    #     self.tracking_id = tracking_id
    #     self.nin = nin
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.middle_name = middle_name
    #     self.gender = gender
    #     self.issued_date = issued_date
    #     self.age_category = age_category

    # def __repr__(self):
    #     return f"(self.name)"

# @app.route('/filtered_query/<nin_val>', methods=['GET'])
@app.route('/filtered_query/<last_name>', methods=['GET'])
def issued_date_request(last_name):
    if request.method == 'GET':
        # nin_data = IssuedDateModel.query.all()
        # nin_val
        # nin_val = 66005354139
        # date_val = 14-1-2020
        query_filter = IssuedDateModel.query.filter_by(nin='last_name').all()
        # query_filter = IssuedDateModel.query.filter_by(nin=date_val).all()
        # query_filter = IssuedDateModel.query.filter_by(nin=nin_val).all_or_404(description='There is no data with {}'.format(nin))
        # query_filter = IssuedDateModel.query.filter_by(nin=nin_val).all()
        # query_filter = IssuedDateModel.query.filter_by(nin='66005354139', issued_date='14-01-2020').all()
        results = [
            {
                "nin": nin.nin,
                "first_name": nin.first_name,
                "last_name": nin.last_name,
                "middle_name": nin.middle_name,
                "issued_date": nin.issued_date
            }
            for nin in query_filter
        ]    

    JSONObjects = {"count": len(results), "query_filter": results}
    return jsonify(JSONObjects)



if __name__ == '__main__':
    app.run(debug=True, port=5000)