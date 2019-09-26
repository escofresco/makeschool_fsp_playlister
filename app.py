from flask import (Flask,
                   render_template)
from pymongo import MongoClient

# Flask simple setup
app = Flask(__name__)
app.config['ENV'] = 'development'

# Mongo setup
client = MongoClient()
playlister_db = client.Playlister
playlist_collection = playlister_db.playlists

@app.route('/')
def playlists_view():
    """Show all playlists."""
    return render_template('playlists_view.html',
                           playlist=playlist_collection.find())

if __name__ == '__main__':
    app.run(debug=True)
