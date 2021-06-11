import flask
import psycopg2
from flask_cors import CORS
from flask import request, jsonify
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

connection = psycopg2.connect(
    host='localhost',
    port="5432",
    database="pet-hotel"
)

CORS(app)

app.route('/')
def hello():
    return 'Hello'

app.route('/api/pets/', methods=['GET'])
def fetch_all_pets():
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    sqlQuery = 'SELECT p.id, o.name, p.name as pet_name, p.breed, p.color, p.checked_in FROM pets p JOIN owner o ON o.id = p.owner_id;'
    cursor.execute(sqlQuery)
    pets = cursor.fetchall()
    print(pets)
    return jsonify(pets)