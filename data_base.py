import sqlite3
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

class Saves:
    def __init__(self):
        self.file_settings = sqlite3.connect(BASE_DIR / 'website_data.db')
        self.cursor = self.file_settings.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self.cursor.fetchall())


    # def __del__(self):
    #     self.file_settings.close()


class SavesDataUsers(Saves):
    # изменение паролья
    # def save_data_user_password(self, value):
    #     self.cursor.execute(f'''UPDATE set_user SET password = {value}''')
    #     self.file_settings.commit()

    def get_data_user(self):
        self.cursor.execute('''SELECT * FROM site_user''')
        columns = [column[0] for column in self.cursor.description]
        users = {}
        for row in self.cursor.fetchall():
            user_dict = dict(zip(columns, row))
            users[user_dict['user_id']] = user_dict

        return users


class SavesDataStudents(Saves):
    def get_data_student(self, user_id):
        self.cursor.execute('''SELECT * FROM student''')
        columns = [column[0] for column in self.cursor.description]
        for row in self.cursor.fetchall():
            student_dict = dict(zip(columns, row))
            if student_dict['user_id'] == user_id:
                return student_dict

i=Saves()