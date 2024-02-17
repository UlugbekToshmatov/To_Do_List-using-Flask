import logging

from pages.back.dtos.list_response import ListResponse
from pages.back.db.database import Database


class ListRepository:
    connection = Database.get_connection()

    def get_all_lists(self):
        get_lists_query = "SELECT * FROM Lists"
        result_set = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_lists_query)
            for entity in cursor:
                result_set.append(
                    ListResponse(
                        id=entity[0],
                        name=entity[1],
                        created_date=entity[2]
                    )
                )

            return result_set
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()

    def get_by_id(self, list_id):
        get_by_id_query = f"SELECT * FROM Lists WHERE id={list_id}"
        result_set = {}
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_by_id_query)
            for entity in cursor:
                result_set['id'] = entity[0]
                result_set['name'] = entity[1]
                result_set['created_date'] = entity[2]

            return result_set
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()

    def create_list(self, name):
        insert_query = f"INSERT INTO Lists (name) VALUE ('{name}')"
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

    def update_by_id(self, list_id, name):
        update_by_id_query = f"UPDATE Lists SET name='{name}' WHERE id={list_id}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_by_id_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
            # self.connection.close()

    def delete_by_id(self, list_id):
        set_deleted_true_query = f"DELETE FROM Lists WHERE id={list_id}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(set_deleted_true_query)
            self.connection.commit()
            return True
        except Exception as e:
            logging.exception(e)
            return False
        # finally:
            # self.connection.close()

    def exists_by_id(self, list_id) -> bool:
        count_by_id_query = f"SELECT count(*) FROM Lists WHERE id={list_id}"
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
