from flask import Blueprint

salary = Blueprint('salary', __name__)
from . import views