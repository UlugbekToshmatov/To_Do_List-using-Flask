from datetime import date

from pages.back.repositories.task_repository import TaskRepository
from pages.back.repositories.list_repository import ListRepository


def get_update_query(task_id, form):
    update_query = f"UPDATE Tasks SET "
    if form['name']:
        update_query += f"name='{form['name']}',"
    else:
        # name cannot be empty
        raise RuntimeError
    if form['notes']:
        update_query += f" notes='{form['notes']}',"
    if form['priority']:
        update_query += f" priority='{form['priority']}',"
    if form['due_date']:
        update_query += f" due_date={date.fromisoformat(form['due_date'])},"
    if form['completed']:
        update_query += f" completed={bool(int(form['completed']))},"

    # leave off the last comma in the query acquired and add the 'WHERE' clause to it
    update_query = update_query[:-1] + f" WHERE id={task_id}"
    return update_query


class TaskService:
    task_repository = TaskRepository()
    list_repository = ListRepository()

    def get_all_by_list_id(self, list_id):
        if not self.list_repository.exists_by_id(list_id):
            raise RuntimeError

        return self.task_repository.get_all_tasks_by_list_id(list_id)

    def get_by_id(self, task_id):
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise RuntimeError

        return task

    def create(self, name, list_id):
        if not name:
            raise RuntimeError

        return self.task_repository.create_task(name, list_id)

    def update_by_id(self, task_id, form):
        if not self.task_repository.exists_by_id(task_id):
            raise RuntimeError

        return self.task_repository.update_by_id(get_update_query(task_id, form))

    def delete_by_id(self, task_id):
        if not self.task_repository.exists_by_id(task_id):
            raise RuntimeError

        return self.task_repository.delete_by_id(task_id)

    def move_to_another_list(self, list_id, task_id):
        if self.list_repository.exists_by_id(list_id) is False or self.task_repository.exists_by_id(task_id):
            raise RuntimeError

        return self.task_repository.move_to_list(list_id, task_id)
