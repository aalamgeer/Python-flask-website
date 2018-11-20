from flask import Flask, session, render_template, request, redirect, url_for, flash
import pymysql, os
from flask_sqlalchemy import SQLAlchemy         # importing sqlalchemy ORM from sqlalchemy
from flask_mail import Mail, Message            # importing flask mail extension
from flask_login import login_manager, UserMixin, login_user, login_required, logout_user, current_user           # importing login module ORM from flask_login
from werkzeug.utils import secure_filename      # importing securty from werkzeug
from datetime import datetime, timedelta                   # importing date from datetime
from forms import BlogForm                      # importing forms from forms.py
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ranaaalamgeer92@gmail.com'
app.config['MAIL_PASSWORD'] = '@alamgeer10'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.secret_key ='Hellothisissecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)

imageFolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = imageFolder


def forDate(): # Function to return year for footer
    now = datetime.now()
    return now.year


def get_ip(): # function return user ip address
    ip = request.remote_addr
    return ip


def checkemail(emailId): # Check email id in table
    connection = pymysql.connect(host="localhost",user="root",password="mynd_helpdesk",db="mooz")
    with connection.cursor() as curser:
        curser.execute("SELECT * FROM users WHERE userEmail LIKE '%"+emailId+"%'")
        numrows = len(curser.fetchall())
        return  numrows


@app.route('/')
def home():
    if 'userName' in session:
        userNameSession = session['userName'].capitalize()
        title = {'title':'Home','year' : forDate(),'userName':userNameSession}
        return render_template('index.html',title=title)
    else:
        title = {'title': 'Home', 'year': forDate()}
        return render_template('login.html', title=title)


@app.route('/about')
def about():
    title = {'title': 'About us', 'year': forDate()}
    if 'userName' in session:
        title['userName'] = session['userName']
        return render_template('about_us.html', title=title)
    else:
        return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    title = {'title': 'Login', 'year': forDate()}
    if 'userName' in session:
        title['userName'] = session['userName']  # Add username in title dictionary
        return render_template('login.html', title=title)
    if request.method == 'GET':
        return render_template('login.html',title= title)
    else:
        userEmail = request.form.get('email')
        password  = request.form.get('password')
        connection = pymysql.connect(host='localhost',user='root',password='mynd_helpdesk',db='mooz')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE userEmail='"+userEmail+"' AND password='"+password+"'")
            result = cursor.fetchall()
            if len(result) == 1:
                session['userName'] = result[0][1]
                return redirect(url_for('home'))
            else:
                flash("Email or password is not correct")
                return redirect(url_for('login'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('userName',None)
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET','POST'])
def signup():
    title ={'title':'Sign up page','year' : forDate()}
    if request.method == 'GET':
        return render_template('signup.html',title=title)
    else:
        email = request.form.get('email')
        name  = request.form.get('name')
        password = request.form.get('password')
        c_password = request.form.get('c_password')
        address = request.form.get('address')
        avatar = str(request.form.get('file'))
        now = datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        if password != c_password:
            error = 'Confirm password is not same as password'
            return render_template('signup.html', title=title, error=error)
        elif checkemail(email):
            error = 'Email id is already exist'
            return render_template('signup.html', title=title, error=error)
        else:
            dbconn = pymysql.connect(host="localhost", user="root", password="mynd_helpdesk", db="mooz")
            curr = dbconn.cursor()
            curr.execute("INSERT INTO users (userName,userEmail,password,address,avatar,created) values ('" + name + "','" + email + "','" + password + "','"+address+"','"+avatar+"','"+now+"')")
            dbconn.commit()
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("You succesfully Signup")
            return redirect(url_for('login'))


@app.route('/reset',methods=['GET', 'POST'])
def reset():
    title = {'title': 'Reset Password', 'year': forDate()}
    if request.method == 'POST':
        toemail = request.form.get('email')
        msg = Message('Subject: Password reset', sender='ranaaalamgeer92@gmail.com', recipients=[toemail])
        msg.body = "Hello change your password"
        mail.send(msg)
        flash("Mail sent to your email address check it.")
        return redirect(url_for('reset'))
    return render_template('reset.html', title=title)


@app.route('/blog')
def blog():
    imageName = os.path.join(app.config['UPLOAD_FOLDER'], 'coding.jpg')
    userImage = os.path.join(app.config['UPLOAD_FOLDER'], 'user.jpg')
    title = {'title': 'Blogs', 'year': forDate(), 'imageName': imageName, 'userImage': userImage}
    if 'userName' in session:
        title['userName'] = session['userName']
        connection = pymysql.connect(host="localhost", user="root", password="mynd_helpdesk", db="mooz")
        with connection.cursor() as curser:
            curser.execute("SELECT * FROM posts")
            result = curser.fetchall()
            curser.execute("SELECT * FROM comment_tbl LIMIT 10")
            comments = curser.fetchall()
            return render_template("blog.html", data=result, comments=comments, title=title)
    else:
        return redirect(url_for('login'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('key')  # type: object
    connection = pymysql.connect(host="localhost",user="root",password="mynd_helpdesk",db="mooz")
    with connection.cursor() as curser:
        curser.execute("SELECT * FROM posts WHERE Auther LIKE '%" + query + "%'")
        result = curser.fetchall()
        if len(result) > 0:
            return str(result)
        else:
            return "<h1>404</h1><br/><h3>Result not found</h3>"


@app.route('/contact_us', methods=['GET', 'POST'])
def contact():
    title = {'title': 'Contact Us', 'year': forDate()}
    if 'userName' in session:
        title['userName'] = session['userName']
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            mobile = request.form.get('mobile')
            subj = request.form.get('subject')
            body = request.form.get('message')
            now = datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            myconn = pymysql.connect(host="localhost", user="root", password="mynd_helpdesk", db="mooz")
            curr = myconn.cursor()
            curr.execute("INSERT INTO contact_us (name,email,mobile,subject,body,created) values ('"+name+"','"+email+"','"+mobile+"','"+subj+"','"+body+"','"+now+"')")
            myconn.commit()
        return render_template('contact.html', title=title)
    else:
        return redirect(url_for('login'))


@app.route('/comment', methods=['GET', 'POST'])
def addComment():
    if request.method == 'POST':
        comment = request.form.get('comment')
        ip = request.remote_addr
        now = datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        dbconn = pymysql.connect(host="localhost",user="root",password="mynd_helpdesk",db="mooz")
        curr = dbconn.cursor()
        curr.execute("INSERT INTO comment_tbl (comment,ip_address,created) values ('"+comment+"','"+ip+"','"+now+"')")
        dbconn.commit()
    return redirect(url_for('blog'))


@app.route('/addBlog', methods=['GET','POST'])
def addBlog():
        title = {'title': 'Add Blog', 'year': forDate()}
        form = BlogForm()
        if form.validate_on_submit():
            '''---------------Add blog to database--------------'''
            blogTitle = request.form.get('blogTitle')
            auther = request.form.get('auther')
            blogContent = request.form.get('blogContent')
            tags = request.form.get('tags')
            now = datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M:%S')
            dbconn = pymysql.connect(host="localhost", user="root", password="mynd_helpdesk", db="mooz")
            curr = dbconn.cursor()
            curr.execute("INSERT INTO posts (userId,title,Auther,post,tags,created) values ('" + '1' + "','" + blogTitle + "','" + auther + "','" + blogContent + "','" + tags + "','" + now + "')")
            dbconn.commit()
            flash("User Adding his blog of {} Title ".format(form.blogTitle.data))
            return redirect(url_for('home'))

        return render_template('addBlog.html',title=title,form=form)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    app.run(debug=True)

