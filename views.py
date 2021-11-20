from os import name
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template("index.html", name="Ivan")

# profile?name=ivan query parameters
@views.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)


@views.route('/profile/<username>')
def profile2(username):
    return render_template("profile.html", name=username)


#return JSON
@views.route('/json')
def get_json():
    data_json = {
        'name': 'Ivan',
        'surname': 'Romero',
        'key': 'rob43b32'
    }
    return jsonify(data_json)


@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)


# redirect
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))



