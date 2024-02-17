from flask import Blueprint, render_template, request, url_for, redirect, flash
from pages.back.services.task_service import TaskService

task_bp = Blueprint("task_bp", __name__, template_folder="../../front/html")
task_service = TaskService()


@task_bp.route("/add/<int:list_id>", methods=['GET', 'POST'])
def add(list_id):
    if request.method == 'GET':
        return render_template("add_task.html", list_id=list_id)
    else:
        created = task_service.create(request.form['name'], list_id)
        if created:
            flash("Task added successfully", "info")
        else:
            flash("Something went wrong. Please, try again.", "error")
        return redirect(url_for("list_bp.get_by_id", list_id=list_id))


@task_bp.route("/update/<int:task_id>", methods=['GET', 'POST'])
def update_by_id(task_id):
    if request.method == 'GET':
        task = task_service.get_by_id(task_id)
        return render_template("update_task.html", task=task)
    else:
        updated = task_service.update_by_id(task_id, request.form)
        if updated:
            flash("Task updated successfully", "info")
        else:
            flash("Something went wrong. Please, try again.", "error")
        return redirect(url_for("task_bp.update_by_id", task_id=task_id, _method='GET'))


@task_bp.route("/delete/<int:list_id>/<int:task_id>")
def delete_by_id(list_id, task_id):
    deleted = task_service.delete_by_id(task_id)
    if deleted:
        flash("Task deleted successfully", "info")
    else:
        flash("Something went wrong. Please, try again.", "error")
    return redirect(url_for("list_bp.get_by_id", list_id=list_id))


@task_bp.route("/move/<int:list_id>/<int:task_id>")
def move_task_to_list(list_id, task_id):
    moved = task_service.move_to_another_list(list_id, task_id)
    if moved:
        flash("Task moved successfully to another list", "info")
    else:
        flash("Something went wrong. Please, try again.", "error")
    return redirect(url_for("list_bp.get_by_id", list_id=list_id))
