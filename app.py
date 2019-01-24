from flask import Flask
from flask import session as ses
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash

app = Flask(__name__)

from database import *

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    print(ses)
    posts =query_all_posts() 
    ''' if 'username' in session:
        return render_template('home_loggedin.html',name="logged in as : " +session['username'],posts=posts)
    else :
        return render_template('home.html',name=" ",posts=posts)
    '''
    return render_template('home.html',name=" ",posts=posts)


@app.route('/create-post',methods=['GET','POST'])
def create_post(): 
    if 'username' in ses:
        if request.method == 'GET':
            return render_template('create_post.html')
        else:
            post_string = request.form['post_submit']
            add_Post(post_string)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('log_in'))
@app.route('/about-us')
def about_us():
    return render_template('aboutus.html')

@app.route('/log-out')
def log_out():

    del ses['username']
    return render_template('home.html',name="",posts=query_all_posts())

@app.route('/log-in', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['psw']
        posts = query_all_posts()
        user = query_by_name_and_password(name, password)
        if user is not None:
            ses['username'] = user.name
            return redirect(url_for('home'))
        else :
            return render_template('log_in.html')
    else:
       return render_template('log_in.html')


'''
@app.route('/create-post', methods=['GET','POST'])
def create_post(): 
    if 'username' in flask_session:
        if request.method == 'GET':
            return render_template('create_post.html')
        else:
            post_string = request.form['post_submit']
            add_Post(post_string)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('log_in'))


@app.route('/about-us')
def about_us():
    return render_template('aboutus.html')



@app.route('/log-out')
def log_out():

    del flask_session['username']
    return render_template('home.html',name="",posts=query_all_posts())



@app.route('/log-in', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['psw']
        posts = query_all_posts()
        user = query_by_name_and_password(name, password)
        if user is not None and user.password == password:
            flask_session['username'] = user.name
            return redirect(url_for('home'))
        else :
            return render_template('log_in.html')
    else:       
        return render_template('log_in.html')
       
        return render_template('log_in.html')

'''

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['username'] 
        password = request.form['psw']
        add_User(name,password)
        flash('You were successfully signed up')
        return redirect(url_for('log_in'))

    else:
        return render_template('sign_up.html')



# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

















