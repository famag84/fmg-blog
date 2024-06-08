from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/get_curve_names', methods=['GET'])
def get_curve_names():
    conn = get_db_connection()
    curves = conn.execute('SELECT DISTINCT curve_name FROM curves').fetchall()
    conn.close()
    curve_names = [curve['curve_name'] for curve in curves]
    return jsonify(curve_names)

@app.route('/fetch_curve', methods=['GET'])
def fetch_curve():
    curve_name = request.args.get('curve_name')
    conn = get_db_connection()
    curve = conn.execute('SELECT point_label, point_value FROM curves WHERE curve_name = ?', (curve_name,)).fetchall()
    conn.close()
    labels = [row['point_label'] for row in curve]
    values = [row['point_value'] for row in curve]
    return jsonify({'labels': labels, 'values': values})

if __name__ == '__main__':
    app.run(debug=True)
