from flask import Flask, render_template, redirect, url_for, request
import psycopg2

app = Flask(__name__)

# Database Configuration
DB_NAME = 'test'
DB_USER = 'lion'
DB_PASSWORD = 'lion'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Connect to the database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to display the Goat_Points view
@app.route('/goat_points')
def display_goat_points():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Goat_Points")
    data = cur.fetchall()
    conn.close()
    return render_template('goat_points.html', data=data)

# Route to display the VaxedGoats view
@app.route('/vaxed_goats')
def display_vaxed_goats():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM VaxedGoats")
    data = cur.fetchall()
    conn.close()
    return render_template('vaxed_goats.html', data=data)

# Route to display the Family_Tree view
@app.route('/family_tree')
def display_family_tree():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Family_Tree")
    data = cur.fetchall()
    conn.close()
    return render_template('family_tree.html', data=data)

# Route to display the Goat_Details view
@app.route('/goat_details', methods=['GET', 'POST'])
def display_goat_details():
    if request.method == 'POST':
        animal_id = request.form['animal_id']
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Goat_Health WHERE animal_id = %s", (animal_id,))
        data = cur.fetchone()
        conn.close()
        return render_template('goat_details.html', data=data)
    return render_template('goat_details_form.html')

if __name__ == '__main__':
    app.run(debug=True)


