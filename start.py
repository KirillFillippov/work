from flask import Flask
from flask_restplus import Resource, Api
from peewee import *

app = Flask(__name__)
api = Api(app)

db = SqliteDatabase('tasks.db')


class Task(Model):
    title = CharField()
    content = CharField()
    created_at = TimeField()

    class Meta:
        database = db


@api.route('/api/task')  # Post
class NewTask(Resource):
    def post(self):


@api.route('/api/task')  # Get
class ListTask(Resource):
    def get(self, title, created_at):
        return title, created_at


@api.route('/api/task/<task_id> ')  # Get
class FullTask(Resource):
    def get(self, title, content, created_at):
        return title, content, created_at


@api.route('/api/task/<task_id>')  # Put
class ChangeTask(Resource):
    def put(self):


@api.route('/api/task/<task_id>')  # Delete
class DelTask(Resource):
    def delete(self):


if __name__ == '__main__':
    app.run(debug=True)

