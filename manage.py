import os
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
<<<<<<< HEAD
from app.api.v1 import models

=======
from app import models
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09


app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()