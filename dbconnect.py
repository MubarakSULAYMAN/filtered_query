from flask import Flask
app = Flask(__name__)

dbms = "postgresql"
username = "postgres"
password = "StrongAdminP@ssw0rd"
server = "localhost"
port = 5342
database = "nin"

dbData = "%(dbms)s://%(username)s:%(password)s@%(server)s:%(port)s/%(database)s"

app.config['SQLALCHEMY_DATABASE_URI'] = dbData


# http://www.nytimes.com/section/nyregion?action=click&pgtype=Homepage
# {
#   'action': 'click',
#   'pgtype': 'Homepage'
# }