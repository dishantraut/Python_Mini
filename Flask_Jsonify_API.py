from flask import Flask , jsonify


app = Flask(__name__)


@app.route('/armstormg/<int:num>')
def arms(num):
    # Python program to check if the number is an Armstrong number or not
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if num == sum:
       result= {
           'Number':num,
           'Armstrong':True,
           'Other Numbers':[1,2,3,4]
           }
    else:
        result={
            'Number':num,
            'Armstrong':False,
            'Other Numbers':[1,2,3,4]
            }

    return jsonify(result)


@app.route('/average/<int:a>/<int:b>')
def avg(a,b):
    c = (a+b)/2
    result = {
        'Average':c,
        'OK':True
        }
    return jsonify(result)


@app.route('/sum/<int:a>/<int:b>')
def add(a,b):
    c = a+b
    result = {
        'Addition':c,
        'OK':True
        }
    return jsonify(result)



@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
    app.run(debug=True,port=8080)



"""
alembic==1.4.3
aniso8601==8.0.0
appdirs==1.4.4
blinker==1.4
cachelib==0.1.1
certifi==2020.6.20
chardet==3.0.4
click==7.1.2
colorclass==2.2.0
cycler==0.10.0
docopt==0.6.2
Flask==1.1.2
Flask-Dance==3.0.0
Flask-DebugToolbar==0.11.0
Flask-Login==0.5.0
Flask-Migrate==2.5.3
Flask-OAuth==0.12
Flask-OAuthlib==0.9.6
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.4
Flask-WTF==0.14.3
gunicorn==20.0.4
heroku==0.1.4
httplib2==0.18.1
idna==2.10
importlib-metadata==2.0.0
itsdangerous==1.1.0
Jinja2==2.11.2
kiwisolver==1.2.0
lazy==1.4
Mako==1.1.3
MarkupSafe==1.1.1
matplotlib==3.3.2
numpy==1.19.2
oauth2==1.9.0.post1
oauthlib==3.1.0
packaging==20.4
pandas==1.1.3
Pillow==8.0.1
pip-review==1.1.0
pip-upgrade==0.0.6
pip-upgrade-outdated==1.5
pip-upgrader==1.4.15
pipdate==0.5.3
pyparsing==2.4.7
python-dateutil==2.8.1
python-editor==1.0.4
pytz==2020.1
requests==2.24.0
requests-oauthlib==1.3.0
six==1.15.0
SQLAlchemy==1.3.20
SQLAlchemy-Utils==0.36.8
terminaltables==3.1.0
urllib3==1.25.11
URLObject==2.4.3
Werkzeug==1.0.1
wincertstore==0.2
WTForms==2.3.3
zipp==3.4.0
"""
