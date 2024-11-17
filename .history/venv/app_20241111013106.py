from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Prikshit@0401',
    'database': 'projectsql'
}

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
        
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insert feedback into the database
        cursor.execute("INSERT INTO Feedback (Rating, Comments, Feedback_date, Customer_id, Flight_id) VALUES (%s, %s, CURDATE(), %s, %s)", 
                       (rating, comments, customer_id, flight_id))
        conn.commit()  # Commit the transaction
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
