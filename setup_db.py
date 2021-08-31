from werkzeug.security import generate_password_hash
import sqlite3

# this file acts as a config for the database values and to set the admin up easy
# server admin can change values of admin and password
default_name = 'admin'
password_hash = generate_password_hash('password')

db = sqlite3.connect('app.db')

db.execute(f'INSERT INTO admin VALUES (0, "{default_name}", "{password_hash}")')
db.commit()
db.close()

print("Admin database setup is completed.")