from flask import Flask, render_template, request, redirect
import sqlite3  # נשתמש ב-sqlite כדי לעבוד עם מסד נתונים קטן

app = Flask(__name__)  # יוצרים את אפליקציית Flask

# פונקציה להתחבר למסד נתונים
def get_db():
    return sqlite3.connect('movies.db')  # מתחברים למסד הנתונים שנקרא movies.db

# פונקציה שיוצרת טבלה אם היא לא קיימת
def create_table():
    db = get_db()  # מתחברים למסד הנתונים
    # יוצרים טבלה בשם movies אם היא לא קיימת
    db.execute('''CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY,  # עמודת ID עם מזהה ייחודי
                    title TEXT,  # עמודת שם הסרט
                    year INTEGER,  # עמודת שנת יציאה
                    rating REAL)''')  # עמודת דירוג
    db.commit()  # שומרים את השינויים למסד הנתונים
    db.close()  # סוגרים את החיבור למסד הנתונים

create_table()  # קוראים לפונקציה פעם אחת כשהאפליקציה מתחילה כדי לוודא שהטבלה קיימת

# עמוד הבית
@app.route('/')
def home():
    return render_template('main.html')  # מציגים את דף הבית (main.html)

# הוספת סרט חדש
@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':  # אם יש בקשת POST (כלומר שמישהו מילא ושלח את הטופס)
        title = request.form['title']  # לוקחים את השם מהטופס
        year = request.form['year']  # לוקחים את השנה מהטופס
        rating = request.form['rating']  # לוקחים את הדירוג מהטופס
        db = get_db()  # מתחברים למסד הנתונים
        # מוסיפים את הסרט החדש לטבלה
        db.execute('INSERT INTO movies (title, year, rating) VALUES (?, ?, ?)', 
                   (title, year, rating))
        db.commit()  # שומרים את השינויים למסד הנתונים
        db.close()  # סוגרים את החיבור
        return redirect('/show')  # מפנים את המשתמש לדף שמציג את הסרטים
    return render_template('add.html')  # אם זו בקשת GET (כלומר כשמישהו נכנס לדף), מציגים את דף ההוספה

# הצגת כל הסרטים
@app.route('/show')
def show_movies():
    db = get_db()  # מתחברים למסד הנתונים
    movies = db.execute('SELECT * FROM movies').fetchall()  # משיגים את כל הסרטים מהטבלה
    db.close()  # סוגרים את החיבור למסד הנתונים
    return render_template('show.html', data=movies)  # מציגים את הסרטים בדף show.html

# מחיקת סרט לפי מזהה
@app.route('/delete/<int:id>', methods=['POST'])
def delete_movie(id):
    db = get_db()  # מתחברים למסד הנתונים
    db.execute('DELETE FROM movies WHERE id = ?', (id,))  # מוחקים את הסרט עם המזהה שקיבלנו
    db.commit()  # שומרים את השינויים למסד הנתונים
    db.close()  # סוגרים את החיבור למסד הנתונים
    return redirect('/show')  # מעבירים את המשתמש חזרה לדף שמציג את הסרטים

# הפעלת האפליקציה
if __name__ == '__main__':
    app.run(debug=True)  # מפעילים את האפליקציה עם מצב debug כדי לעזור בתיקון שגיאות