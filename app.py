from flask import Flask, render_template, request
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/bands', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def bands():
    if request.method == "POST":
        bandName = request.form['bandName']
        numMembers = request.form['numMembers']
        genre = request.form['genre']

        if bandName == '':
            bandName = None
        if numMembers == '':
            numMembers = None
        if genre == '':
            genre = None
        
        insertQuery = "INSERT INTO `Bands` (`bandName`, `numMembers`, `genre`) VALUES (%s,%s,%s);"
        insertTuple = (bandName, numMembers, genre)
        insertCursor = db.execute_query(db_connection=db_connection, query=insertQuery, query_params=insertTuple) 
    
    elif request.method == "PUT":
        print('we want to modify some data')
    
    elif request.method == "DELETE":
        print('we want to delete some data')

    query = "SELECT * from Bands;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    print(results)
    return render_template("bands.j2", Bands=results)

@app.route('/events', methods = ['POST', 'GET', 'PUT', 'DELETE'])
def events():
    if request.method == "POST":
            eventName = request.form['eventName']
            eventDate = request.form['eventDate']
            eventType = request.form['eventType']
            eventLocation = request.form['eventLocation']
            eventCity = request.form['eventCity']
            eventState = request.form['eventState']

            if eventName == '': eventName = None
            if eventDate == '': 
                eventDate = None
            elif eventDate != '':
                date = eventDate[0:10]
                time = eventDate[11:]
                time += ':00'
                eventDate = date + ' ' + time
            if eventType == '': eventType = None
            if eventLocation == '': eventLocation = None
            if eventCity == '': eventCity = None
            if eventState == '': eventState = None

            insertQuery = "INSERT INTO `Events` (`eventName`, `eventDate`, `eventType`, `eventLocation`, `eventCity`, `eventState`) VALUES (%s,%s,%s,%s,%s,%s);"
            insertTuple = (eventName, eventDate, eventType, eventLocation, eventCity, eventState)
            insertCursor = db.execute_query(db_connection=db_connection, query=insertQuery, query_params=insertTuple) 
        
    query = "SELECT * from Events;"    
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    print(results)
    return render_template("events.j2", Events=results)

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    app.run(port=port, debug=True) 