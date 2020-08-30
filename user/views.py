from flask import Blueprint
from user.models import User

user_bp = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='./templates'
)


@user_bp.route('/register')
def register():
    pass


@user_bp.route('/login')
def login():
    pass


@user_bp.route('/info')
def info():
    pass


@user_bp.route('/logout')
def logout():
    pass
