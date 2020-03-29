from flask import Flask
from flask_cqlalchemy import CQLAlchemy
import uuid
app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "techfossguru"
db = CQLAlchemy(app)




class Persons(db.Model):
    __keyspace__ = 'techfossguru'
    uid = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    name = db.columns.Text(primary_key=True)
    addr = db.columns.Text()


@app.route('/')
def show_user():
    persons = Persons.objects().first()
    return  persons.name


if __name__ == '__main__':
    app.run()
