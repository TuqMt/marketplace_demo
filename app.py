
from datetime import date
from flask import Flask, render_template, redirect, url_for, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="testbase",
        user="postgres",
        password="MatvaFd09",
        host="localhost",
        port="5432"
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/items')
def items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, price, category, image_url FROM items")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    products = [{
        'name': row[0],
        'description': row[1],
        'price': row[2],
        'category': row[3],
        'image_url': row[4]
    } for row in rows]

    return render_template('index.html', products=products)


@app.route('/buy/<name>', methods=['POST'])
def buy(name):
    conn = get_db_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT price FROM items WHERE name = %s", (name,))
    result = cursor.fetchone()
    if result:
        price = result[0]
        cursor.execute(
            "INSERT INTO buys (date, name, price) VALUES (%s, %s, %s)",
            (date.today(), name, price)
        )
        conn.commit()

    cursor.close()
    conn.close()
    return redirect(url_for('items'))

@app.route('/profile')
def profile():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, name, price FROM buys ORDER BY date DESC")
    purchases = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('profile.html', purchases=purchases)

if __name__ == '__main__':
    app.run(debug=True)
