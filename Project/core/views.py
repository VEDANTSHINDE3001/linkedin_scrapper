from flask import render_template,request,Blueprint, session, flash, redirect, url_for
core = Blueprint("core", __name__)

@core.route('/home')
def index():
    #return render_template('index.html')
    return "Hello man"