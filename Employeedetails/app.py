from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pass@123",
    database="omkar_db"
)

# Define the endpoint for the form
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Extract data from the form
        emp_name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        department = request.form['department']
        
        # Insert data into the MySQL database
        cursor = db.cursor()
        sql = "INSERT INTO employees (emp_name, email, phone, age, department) VALUES (%s, %s, %s, %s, %s)"
        val = (emp_name, email, phone, age, department)
        cursor.execute(sql, val)
        db.commit()
        
        # Return a success message
        return "Employee details submitted successfully!"
    
    # Render the HTML form
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
