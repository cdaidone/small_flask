from hp_characters import CHARACTERS
from flask import Flask, render_template
app = Flask(__name__)


def get_names(source):
    names = []
    for row in source:
        name = row["Name"]
        names.append(name)
    return names


def get_character_details(source, name):
    for row in source:
        name = row["Name"]
        house = row["House"]
        blood_status = row["blood_status"]
        if name == row["Name"]:
            house = row["House"]
            blood_status = row["blood_status"]
            return name, house, blood_status


def test(source):
    for s in CHARACTERS:
        name = s["Name"]
        print name


character_list = get_names(CHARACTERS)
name = test(CHARACTERS)
name, house, blood_status = get_character_details(CHARACTERS, name)
#print character_list
#print name

@app.route('/characters')
def characters():
    return render_template('main_app.html', character_list=character_list, name=name)

@app.route('/characters/<name>')
def details(name):
    return render_template('character_app.html', name=name, house=house, blood_status=blood_status)


if __name__ == '__main__':
    app.run(debug=True)
