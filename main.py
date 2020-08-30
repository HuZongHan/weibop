from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp

# 初始化 app
app = Flask(__name__)
app.secret_key = r'#%$#@^&IGugu^$^%$&U&ikjihiu^&^T&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hzh:HZHh123!@140.143.234.185:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 初始化 manager
Manager = Manager(app)

# 初始化 db 和migrate
db.init_app(app)
migrate = Migrate(app, db)
Manager.add_command('db', MigrateCommand)

# 注册蓝图
app.register_blueprint(user_bp)


@app.route('/')
def home():
    return 'hello'


if __name__ == '__main__':
    Manager.run()
