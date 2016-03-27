from hp_characters import CHARACTERS
from flask import Flask, render_template
app = Flask(__name__)


def get_names(source):
    names = []
    for row in source:
        name = row["Name"]
        names.append(name)
    return sorted(names)


def get_character_details(source, name):
    for row in source:
        if name == row["Name"]:
           house = row["House"]
           blood_status = row["blood_status"]
           return name, house, blood_status

character_list = get_names(CHARACTERS)

def test(source):
    for row in source:
        name = row["Name"]
    return name

name = test(CHARACTERS)
name, house, blood_status = get_character_details(CHARACTERS, name)

@app.route('/')
def characters():
    return render_template('main_app.html', character_list=character_list, name=name)

@app.route('/characters/<a>')
def details(a):
    return render_template('character_app.html', name=name, house=house, blood_status=blood_status)


if __name__ == '__main__':
    app.run(debug=True)
