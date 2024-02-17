from pages.back.db.database import Database
from pages.back.dtos.task_response import TaskResponse
import logging


class TaskRepository:
    connection = Database.get_connection()

    def get_all_tasks_by_list_id(self, list_id):
        get_tasks_by_list_id_query = f"SELECT * FROM Tasks WHERE list_id={list_id}"
        result_set = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_tasks_by_list_id_query)
            for entity in cursor:
                result_set.append(
                    TaskResponse(
                        id=entity[0],
                        name=entity[1],
                        notes=entity[2],
                        priority=entity[3],
                        due_date=entity[4],
                        completed=bool(entity[5]),
                        created_date=entity[6],
                        list_id=entity[8]
                    )
                )

            return result_set
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()

    def get_by_id(self, task_id):
        get_by_id_query = f"SELECT * FROM Tasks WHERE id={task_id}"
        task = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_by_id_query)
            for entity in cursor:
                task = TaskResponse(
                    id=entity[0],
                    name=entity[1],
                    notes=entity[2],
                    priority=entity[3],
                    due_date=entity[4],
                    completed=bool(entity[5]),
                    created_date=entity[6],
                    list_id=entity[8]
                )

            return task
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()

    def create_task(self, name, list_id):
        insert_query = f"INSERT INTO Tasks (name, list_id) VALUES ('{name}', {list_id})"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
        # self.connection.close()

    def update_by_id(self, update_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
        # self.connection.close()

    def delete_by_id(self, task_id):
        delete_query = f"DELETE FROM Tasks WHERE id={task_id}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
        # self.connection.close()

    def move_to_list(self, list_id, task_id):
        update_list_id_query = f"UPDATE Tasks SET list_id={list_id} WHERE id={task_id}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_list_id_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
            # self.connection.close()

    def exists_by_id(self, task_id):
        count_by_id_query = f"SELECT count(*) FROM Tasks WHERE id={task_id}"
        quantity = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(count_by_id_query)
            for qty in cursor:
                quantity = qty[0]

            return quantity > 0
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        # self.connection.close()
