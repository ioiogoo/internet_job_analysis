from flask import Blueprint

python = Blueprint('python', __name__)

from . import views
