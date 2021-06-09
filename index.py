from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

# PostgreSQL Database credentials loaded from the .env file
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

app = Flask(__name__)

# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)

try:
    con = psycopg2.connect(
        database=DATABASE,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)

    cur = con.cursor()

    # GET: Fetch all movies from the database
    @app.route('/')
    def fetch_all_pets():
    
        # SQL query to get data from pets / owner table
        cur.execute('SELECT * FROM pets p JOIN "owner" o ON o.id = p.owner_id;')
        rows = cur.fetchall()
        
        # Empty array to hold pet data
        pet_data = []

        # Loop over rows from DB
        for row in rows:
            pet_data.append({
                'pet_id': row[0],
                'owner_id': row[1],
                'name': row[2],
                'breed': row[3],
                'color': row[4],
                'checked_in': row[5],
                'checked_in_date': row[6],
                'owner_name': row[8]
            })
            # To change above data structure, check the index and adjust accordingly
            print(rows)

        # From this end point, return the pet_data array
        return jsonify(pet_data)
    
    # MORE ROUTES HERE!!

    # MORE ROUTES HERE !!
except:
    print('Error')