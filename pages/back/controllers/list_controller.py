from flask import Blueprint, render_template
from pages.back.services.list_service import ListService


list_bp = Blueprint("list_bp", __name__, template_folder="../../front")
list_service = ListService()


@list_bp.route("/")
def index():
    response_list = list_service.get_all_lists()
    return render_template("index.html", response_list=response_list)
