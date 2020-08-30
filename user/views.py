import datetime
from flask import Blueprint
from flask import request
from flask import render_template
from user.models import User
from libs.utils import make_password
from libs.orm import db
user_bp = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='./templates'
)


@user_bp.route('/register', methods=('POST', 'GER'))
def register():
    if request.method == 'POST':
        nickname = request.form.get('', '').strip()
        password1 = request.form.get('', '').strip()
        password2 = request.form.get('', '').strip()
        gender = request.form.get('', '').strip()
        birthday = request.form.get('', '').strip()
        city = request.form.get('', '').strip()
        bio = request.form.get('', '').strip()
        now = datetime.datetime.now()


        if not password1 or password1 != password2:
            return render_template('register.html',err='密码不符合要求')
        user = User(nickname=nickname,gender=gender,created=now,
                    birthday=birthday,city=city,bio=bio,password=make_password(password1))


        # 保存头像
        avatar = request.file.get('')

        db.session.add(user)
        db.session.commit()

    else:
        return render_template('register.html')


@user_bp.route('/login')
def login():
    pass


@user_bp.route('/info')
def info():
    pass


@user_bp.route('/logout')
def logout():
    pass
