from flask import (Flask,
                   render_template)

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_view.html',
                           playlist=[{
                             'title': 'Cat Videos',
                             'description': 'Cats acting weird'
                            },
                            {
                                'title': '80\'s Music',
                                'description': 'Don\'t stop believing!'
                            }])

if __name__ == '__main__':
    app.run(debug=True)
