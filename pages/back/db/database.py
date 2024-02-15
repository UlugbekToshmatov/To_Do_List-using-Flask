import logging

import mysql.connector


class Database:
    @staticmethod
    def get_connection():
        logging.log(10, "Connected to db successfully")
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="to_do_list_db"
        )
