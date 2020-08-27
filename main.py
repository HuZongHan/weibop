from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from libs.orm import db

# 初始化 app
app = Flask(__name__)
app.secret_key = r'#%$#@^&IGugu^$^%$&U&ikjihiu^&^T&'
app.config['SQLALCHEMY_DATABASE_RLI'] = 'mysql+pymysql://HZH:HZHh123!@10.0.2.15:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 初始化 manager
Manager = Manager(app)

# 初始化 db 和migrate
db.init_app(app)
migrate = Migrate(app, db)
Manager.add_command('db', MigrateCommand)


@app.route('/')
def home():
    return 'hello'


if __name__ == '__main__':
    Manager.run()
