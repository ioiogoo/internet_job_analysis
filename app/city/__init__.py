from flask import Blueprint

city = Blueprint('city', __name__)
from . import views