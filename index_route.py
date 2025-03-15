from flask import Blueprint, render_template
from sqlalchemy import insert, select
from .database import db


# HTML FILES

INDEX_HTML = 'index.html'
homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route("/")
def homepage():
    return render_template(INDEX_HTML)

