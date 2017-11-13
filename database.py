import datetime


from peewee import *  # space between third party libraries

db = SqliteDatabase('work_log.db')


class Log(Model):
    """Instantiates and governs local instance of database"""
    timestamp = DateTimeField(default=datetime.datetime.now)
    user_name = CharField(max_length=255, unique=True)
    task_name = CharField(max_length=255)
    task_time = IntegerField(default=0)
    notes = TextField()

    class Meta:
        database = db

    def initialize(self):
        """Create table and database if they don't exist"""
        db.connect()
        db.create_tables([self], safe=True)
