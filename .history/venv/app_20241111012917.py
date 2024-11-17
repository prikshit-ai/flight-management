from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Prikshit@0401'
app.config['MYSQL_DB'] = 'projectsql'

mysql = MySQL(app)

# Route for home or login page
@app.route('/')
def home():
    return render_template('login.html')

# Route for customer dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for submitting feedback
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        rating = request.form['rating']
        comments = request.form['comments']
        customer_id = request.form['customer_id']
        flight_id = request.form['flight_id']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Feedback (Rating, Comments, Feedback_date, Customer_id, Flight_id) VALUES (%s, %s, CURDATE(), %s, %s)", 
                       (rating, comments, customer_id, flight_id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
