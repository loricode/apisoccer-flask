from flask import Flask,request,jsonify #pip install Flask
import psycopg2  #pip install psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS #pip install flask-cors

app = Flask(__name__)
CORS(app)

def conexion():
    return psycopg2.connect(
    host="localhost",
    database="dbteam",
    user="postgres",
    password="cuadrado")

@app.route('/api',  methods=['GET'])
def index():
    conn = conexion()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM teamfootball ORDER BY name")
    rows = cur.fetchall() 
    conn.close()
    cur.close()
    return jsonify(rows)


@app.route('/api', methods=['POST'])
def saveTeam():
	conn = conexion()
	cur = conn.cursor()
	data = request.json
	sql = """INSERT INTO teamfootball (name, trophy, image ) 
             VALUES (%(name)s, %(trophy)s, %(image)s)"""
	cur.execute(sql, data) 
	conn.commit() 
	conn.close()
	cur.close()       
	return jsonify(msg='added successfully!') 
	
	
    	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
