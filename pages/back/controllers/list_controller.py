from flask import Blueprint, render_template, request, url_for, redirect, flash
from pages.back.services.list_service import ListService
from pages.back.services.task_service import TaskService

list_bp = Blueprint("list_bp", __name__, template_folder="../../front/html")
list_service = ListService()
task_service = TaskService()


@list_bp.route("/")
def index():
    response_list = list_service.get_all_lists()
    return render_template("index.html", response_list=response_list)


@list_bp.route("/<int:list_id>")
def get_by_id(list_id):
    response = list_service.get_by_id(list_id)
    lists = list_service.get_lists_except_for(list_id)
    tasks = task_service.get_all_by_list_id(list_id)
    return render_template("get_list.html", response=response, lists=lists, tasks=tasks)


@list_bp.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template("add_list.html")
    else:
        created = list_service.create_list(request.form["name"])
        if created:
            flash("List created successfully", "info")
        else:
            flash("Something went wrong. Please, try again.", "error")
        return redirect(url_for("list_bp.index"))


@list_bp.route("/update/<int:list_id>", methods=['GET', 'POST'])
def update_by_id(list_id):
    if request.method == 'GET':
        list_response = list_service.get_by_id(list_id)
        return render_template("update_list.html", response=list_response)
    else:
        updated = list_service.update_by_id(list_id, request.form['name'])
        if updated:
            flash("List updated successfully", "info")
        else:
            flash("Something went wrong. Please, try again.", "error")
        return redirect(url_for("list_bp.update_by_id", list_id=list_id, _method='GET'))


@list_bp.route("/delete/<int:list_id>")
def delete_by_id(list_id):
    deleted = list_service.delete_by_id(list_id)
    if deleted:
        flash("List deleted successfully", "info")
    else:
        flash("Something went wrong. Please, try again.", "error")
    return redirect(url_for("list_bp.index"))
