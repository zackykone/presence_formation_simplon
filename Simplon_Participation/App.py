from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Akamco1@mour',
    'database': 'simplon_participation'
}

# MySQL connection setup
db_connection = mysql.connector.connect(**db_config)

# Routes
@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # Retrieve participant information from the form
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        email = request.form['email']

        # Save participant information to the database
        cursor = db_connection.cursor()
        query = "INSERT INTO participants (nom, prenom, telephone, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nom, prenom, telephone, email))
        db_connection.commit()

        # Redirect to the participant list page
        return redirect('/participants')

    return render_template('register.html')

@app.route('/participants')
def participants():
    cursor = db_connection.cursor()
    query = "SELECT * FROM participants"
    cursor.execute(query)
    participants = cursor.fetchall()

    return render_template('participants.html', participants=participants)

# Run the Flask application
if __name__ == '__main__':
    app.run()
