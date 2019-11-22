from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Stephen Kamau',
        'title': 'My Fist Post',
        'content': 'This is my first blog post',
        'date':'Jan 2, 2019'

    },
     {
        'author': 'Jane Doe',
        'title': 'My Fist Post',
        'content': 'This is my first blog post',
        'date':'Jan 3, 2019'

    }

]

@app.route('/') 
@app.route('/home')
def home():
    return render_template('index.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)