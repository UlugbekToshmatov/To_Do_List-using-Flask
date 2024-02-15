import logging

from pages.back.dtos.list_response import ListResponse
from pages.back.db.database import Database


class ListRepository:
    connection = Database.get_connection()

    def get_all_lists(self):
        get_lists_query = "SELECT * FROM Lists WHERE deleted=false"
        result_set = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_lists_query)
            for entity in cursor:
                result_set.append(
                    ListResponse(
                        entity[0],
                        entity[1],
                        entity[2]
                    )
                )

            return result_set
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()

    def create_list(self, name):
        insert_query = f"INSERT INTO Lists (name) VALUE ({name})"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query)
            self.connection.commit()
        except Exception as e:
            logging.exception(e)
            return None
        # finally:
        #     self.connection.close()
