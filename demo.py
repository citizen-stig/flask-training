from flask import Flask
from models import db, User
from config import EnvironmentConfig


app = Flask(__name__)
app.config.from_object(EnvironmentConfig)
db.app = app
db.init_app(app)

@app.route('/')
def hello_world():
    if User.query.count() > 0:
        return 'Say hello to: ' + ''.join([str(user) for user in User.query.all()])
    else:
        return 'No users, stay tuned.'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
