
from flask import Flask, request
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__, static_url_path='')
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'enter6134'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.246.83'
mysql.init_app(app)
# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add/<username>/<email>")
def add(username , email) :
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO students (studentName, email) values ('%s','%s')''' % (username, email)) 
	cur.execute('commit;')
	return 'added :)'

@app.route("/update/<name1>/<name2>")
def update(name1, name2) :
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE students SET studentName = '%s'  WHERE studentName LIKE '%s' ''' % (name1 , name2))
        cur.execute('commit;')
        return 'All Hail King Steve'

@app.route("/delete/<name>")
def delete(name) :
	cur = mysql.connection.cursor()
	cur.execute('''DELETE from students WHERE studentName LIKE '%s' ''' % (name))
	cur.execute('commit;')
	return 'RIP STEVE'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')

@app.route('/lmao')
def root():
    return app.send_static_file('index.html')
