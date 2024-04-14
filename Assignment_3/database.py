import sqlite3

class TaskDB:
    def __init__(self):
        self.conn = sqlite3.connect('Question3_Supporting_Files/task_list_db.sqlite')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                completed INTEGER DEFAULT 0
                                )''')
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM Task")
        tasks = self.cursor.fetchall()
        return [{'id': task[0], 'description': task[1], 'completed': task[2]} for task in tasks]

    def add_task(self, task_description):
        self.cursor.execute("INSERT INTO Task (description, completed) VALUES (?, ?)", (task_description, 0))
        self.conn.commit()

    def complete_task(self, task_id):
        self.cursor.execute("UPDATE Task SET completed = ? WHERE id = ?", (1, task_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM Task WHERE id = ?", (task_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0