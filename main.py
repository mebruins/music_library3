from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime

app = Flask(__name__)

# Create database if it doesn't already exist
def create_music_library_table():
    conn = sqlite3.connect("music_library.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS music_library (
              id INTEGER PRIMARY KEY,
              title TEXT,
              composer TEXT,
              ensemble TEXT,
              date_performed DATE
              )''')
    
    conn.commit()
    conn.close()

# Add files to toe music library database
def add_music(title, composer, ensemble, date_performed):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    date_performed_str = date_performed.strftime('%Y-%m-%d')

    c.execute("INSERT INTO music_library (title, composer, ensemble, date_performed) VALUES (?, ?, ?, ?)", (title, composer, ensemble, date_performed_str))
    conn.commit()
    conn.close()

# The follow functions enable user to search by any of the data (columns) in the DB
def search_by_title(title):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM music_library WHERE title = ?", (title,))
    results = c.fetchall()
    conn.close()

    if results:
        music_data_list = []
        for result in results:
            music_data = {
                'id': result[0],
                'title': result[1],
                'composer': result[2],
                'ensemble': result[3],
                'date_performed': result[4],
            }
            music_data_list.append(music_data)
        return music_data_list
    else:
        return None

def search_by_composer(composer):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM music_library WHERE composer = ?", (composer,))
    results = c.fetchall()
    conn.close()

    if results:
        music_data_list = []
        for result in results:
            music_data = {
                'id': result[0],
                'title': result[1],
                'composer': result[2],
                'ensemble': result[3],
                'date_performed': result[4],
            }
            music_data_list.append(music_data)
        return music_data_list
    else:
        return None
    
def search_by_ensemble(ensemble):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM music_library WHERE ensemble = ?", (ensemble,))
    results = c.fetchall()
    conn.close()

    if results:
        music_data_list = []
        for result in results:
            music_data = {
                'id': result[0],
                'title': result[1],
                'composer': result[2],
                'ensemble': result[3],
                'date_performed': result[4],
            }
            music_data_list.append(music_data)
        return music_data_list
    else:
        return None
    
def search_by_date_performed(date_performed):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM music_library WHERE date_performed = ?", (date_performed,))
    results = c.fetchall()
    conn.close()

    if results:
        music_data_list = []
        for result in results:
            music_data = {
                'id': result[0],
                'title': result[1],
                'composer': result[2],
                'ensemble': result[3],
                'date_performed': result[4],
            }
            music_data_list.append(music_data)
        return music_data_list
    else:
        return None

# Edit previous data
def edit_music_by_title(title):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM music_library WHERE title=?", (title,))
    result = c.fetchone()
    conn.close()

    if result:
        music_data = {
            'id': result[0],
            'title': result[1],
            'composer': result[2],
            'ensemble': result[3],
            'date_performed': result[4],
        }
        return music_data
    else:
        return None

def update_music(id, new_title, composer, ensemble, date_performed):
    conn = sqlite3.connect('music_library.db')
    c = conn.cursor()

    c.execute("UPDATE music_library SET title=?, composer=?, ensemble=?, date_performed=? WHERE id =?", (new_title, composer, ensemble, date_performed, id))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_music', methods=['POST'])
def add_music_route():
    title = request.form['title']
    composer = request.form['composer']
    ensemble = request.form['ensemble']
    date_performed_str = request.form['date_performed']
    date_performed = datetime.datetime.strptime(date_performed_str, '%Y-%m-%d').date()
    add_music(title, composer, ensemble, date_performed)
    return redirect(url_for('index'))

@app.route('/search_title', methods=['POST', 'GET'])
def search_by_title_route():
    if request.method == 'POST':
        try:
            title = request.form['search_title']
            results = search_by_title(title)

            if results:
                return render_template('search_result.html', results=results, search_type='title')
            else: 
                return render_template('file_not_found.html', search_type='title')
        except KeyError:
            return render_template('file_not_found.html', search_type='title')
    else:
        return redirect(url_for('index'))
        
@app.route('/search_composer', methods=['POST', 'GET'])
def search_by_composer_route():
    if request.method == 'POST':
        try:
            composer = request.form['search_composer']
            results = search_by_composer(composer)

            if results:
                return render_template('search_result.html', results=results, search_type='composer')
            else: 
                return render_template('file_not_found.html', search_type='composer')
        except KeyError:
            return render_template('file_not_found.html', search_type='composer')
    else:
        return redirect(url_for('index'))
           
@app.route('/search_ensemble', methods=['POST', 'GET'])
def search_by_ensemble_route():
    if request.method == 'POST':
        try:
            ensemble = request.form['search_ensemble']
            results = search_by_ensemble(ensemble)

            if results:
                return render_template('search_result.html', results=results, search_type='ensemble')
            else: 
                return render_template('file_not_found.html', search_type='ensemble')
        except KeyError:
            return render_template('file_not_found.html', search_type='ensemble')
    else:
        return redirect(url_for('index'))

@app.route('/search_date_performed', methods=['POST', 'GET'])
def search_by_date_performed_route():
    if request.method == 'POST':
        try:
            date_performed = request.form['search_date_performed']
            results = search_by_date_performed(date_performed)

            if results:
                return render_template('search_result.html', results=results, search_type='date_performed')
            else: 
                return render_template('file_not_found.html', search_type='date_performed')
        except KeyError:
            return render_template('file_not_found.html', search_type='date_performed')
    else:
        return redirect(url_for('index'))

@app.route('/edit_music', methods=['GET', 'POST'])
def edit_music_by_title_route():
    if request.method == 'POST':
        title = request.form['title']
        result = edit_music_by_title(title)

        if result:
            return render_template('edit_music.html', result=result)
        else:
            return render_template('file_not_found.html')
    
    else:
        return render_template('edit_music.html')

@app.route('/update_music', methods=['POST'])
def update_music_route():
    id = request.form['id']
    new_title = request.form['new_title']
    composer = request.form['composer']
    ensemble = request.form['ensemble']
    date_performed_str = request.form['date_performed']

    date_performed = datetime.datetime.strptime(date_performed_str, '%Y-%m-%d').date()
    update_music(id, new_title, composer, ensemble, date_performed)

    return redirect(url_for('index'))

if __name__ == "__main__":
    create_music_library_table()
    app.run(debug=True)
