from flask import Blueprint, render_template, abort, redirect
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__, template_folder='views')

@main.route('/')
def index():
    return render_template('index.html', user='', title="Home")

@main.route('/profile')
def profile():
    return render_template('profile.html', user='', title="Profile")

@main.route('/gallery')
def gallery():
    return render_template('gallery.html', user='', title="Gallery")

@main.route('/upload')
def upload():
    return render_template('upload.html', user='', title="Upload")

@main.route('/login')
def login():
    return render_template('login.html', user='', title="Login")

@main.route('/logout')
def logout():
    return redirect('/login')

@main.route('/register')
def register():
    return render_template('register.html', user='', title="Register")


