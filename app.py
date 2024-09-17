from flask import Flask, render_template, request, redirect, url_for
import sqlite3

api = Flask(__name__)

# פונקציה להתחברות לבסיס הנתונים
def get_db_connection():
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row  # הופך את השורות למילון
    return con

# יצירת טבלה אם היא לא קיימת
def create_table():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    rating REAL NOT NULL)''')
    con.commit()
    con.close()

create_table()

# דף הבית
@api.route('/', methods=['GET'])
def get_main():
    return render_template('main.html')

# נתיב להוספת סרטים
@api.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        title = request.form['title']  # שימוש בטופס HTML
        year = request.form['year']
        rating = request.form['rating']
        
        con = get_db_connection()
        cur = con.cursor()
        cur.execute('''INSERT INTO movies (title, year, rating) VALUES (?, ?, ?)''',
                    (title, year, rating))
        con.commit()
        con.close()
        
        return redirect(url_for('show_data'))
    else:
        return render_template('add.html')

# נתיב להצגת רשימת הסרטים
@api.route('/show', methods=['GET'])
def show_data():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()  # משיג את כל השורות
    con.close()
    return render_template('show.html', data=movies)

# נתיב למחיקת סרט לפי מזהה
@api.route('/delete/<int:id>', methods=['POST'])
def delete_movie(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute('DELETE FROM movies WHERE id = ?', (id,))
    con.commit()
    con.close()
    return redirect(url_for('show_data'))

if __name__ == '__main__':
    api.run(debug=True)