from bson.objectid import ObjectId
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient

# Flask simple setup
app = Flask(__name__)
app.config["ENV"] = "development"

# Mongo setup
client = MongoClient()
playlister_db = client.Playlister
playlist_collection = playlister_db.playlists


@app.route("/")
def playlists_view():
    """Show all playlists."""
    return render_template("playlists_view.html", playlists=playlist_collection.find())


@app.route("/playlists", methods=['POST'])
def playlists_submit():
    """Handle save playlist form action"""
    playlist_document = {
        'title': request.form.get('title-input'),
        'description': request.form.get('description-input'),
        'videos': request.form.get('videos-input').split(),
    }
    playlist_collection.insert_one(playlist_document)
    return redirect(url_for("playlists_view"))

@app.route("/playlists/<playlist_id>")
def playlists_show(playlist_id):
    playlist = playlists.find_one({"_id": ObjectId(playlist_id)})
    return render_template("playlists_show.html", playlist=playlist)

@app.route("/playlists/new")
def playlists_new():
    """Create a playlist"""
    return render_template("playlists_new.html")


if __name__ == "__main__":
    app.run(debug=True)
