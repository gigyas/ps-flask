from flasky import app, db
from flasky.models import User

from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    print('Initialized the database')

@manager.command
def dropdb():
    if prompt_bool('Drop all data?'):
        db.drop_all()
        print('Dropped database')

if __name__ == '__main__':
    manager.run()