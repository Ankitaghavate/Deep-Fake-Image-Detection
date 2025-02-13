from flask import Flask, render_template, jsonify
#import mysql.connector
'''

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ankita@9090",
    database="mydatabases",
    auth_plugin="caching_sha2_password"  # Use this instead
)


@app.route('/gettable', methods=['GET'])
def get_tables():
    try:
        cursor = con.cursor()  # Fixed: Added parentheses to create cursor
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        cursor.close()
        
        table_names = [table[0] for table in tables]  # Fixed: Corrected list comprehension
        return jsonify({"Tables": table_names}), 200
    except mysql.connector.Error as err:
        return jsonify({"Error": str(err)}), 500
'''
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def Home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=9090)
