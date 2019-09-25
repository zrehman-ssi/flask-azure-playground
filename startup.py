import os
from app.main import create_app, db
from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app()

app.app_context().push()
app.register_blueprint(blueprint)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()