import os
from app.main import create_app, db
from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy_utils import create_database, database_exists

app = create_app()

app.app_context().push()
app.register_blueprint(blueprint)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    url = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(url):
        create_database(url)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()