import sqlite3
import pandas as pd

con = sqlite3.connect('database.sqlite')
cur = con.cursor()

def create_table(master_password_hash):
  cur.execute('CREATE TABLE IF NOT EXISTS data(app text, password text, email text, username text, url text)')
  #cur.execute('INSERT INTO data(app, password) VALUES(?,?)', (master_name, master_password_hash))

##########################
  
def insert_data_table(app_name,password_create, user_email, username, url):
  # Insert a row of data
  cur.execute("INSERT INTO data (app, password, email, username, url) VALUES(?, ?, ?, ?, ?)", 
                                                  (app_name,password_create, user_email, username, url)) 
  # Save (commit) the changes
  con.commit()
  con.close()
  
########################## 

def consult_app(input):
  cur.execute("SELECT * FROM data WHERE app = ?", (input,)) 
  result = cur.fetchall()
  result = pd.DataFrame(result)
  result.columns = ['app', 'password', 'email', 'username', 'url']
  print(result)
  
##########################

def consult_email(input):
  cur.execute("SELECT * FROM data WHERE email = ?", (input,))
  result = cur.fetchall()
  result = pd.DataFrame(result)
  result.columns = ['app', 'password', 'email', 'username', 'url']
  print(result) 

##########################  
  
def consult_table():
  cur.execute('SELECT * FROM data')
  result = cur.fetchall()
  result = pd.DataFrame(result)
  result.columns = ['app', 'password', 'email', 'username', 'url']
  
  print(result)   
##########################
  
a = 'facebook'
#create_table() 
#consult_app(a)