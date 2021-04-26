from flask import Flask, render_template
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

# @app.route('/bsg-people')
# def bsg_people():
#     query = "SELECT * FROM bsg_people;"
#     cursor = db.execute_query(db_connection=db_connection, query=query)
#     results = cursor.fetchall()
#     return render_template("bsg.j2", bsg_people=results)

@app.route('/bands')
def bands():
    query = "SELECT * from Bands;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("bands.j2", Bands=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 