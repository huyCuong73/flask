from flask_restful import Resource
from flask import request, jsonify

from model import ToDoList

class ListController(Resource):

    # params: {userId:String}
    def get(self,userId):
        return jsonify(ToDoList.getList(userId))
 

    # args: {userId:String, date:String, start:String, task:String}  
    def post(self):
        userId = request.form['userId']
        date = request.form['date']
        start = request.form['start']
        task = request.form['task']

        return jsonify(ToDoList.createTask(userId, date, start, task))


    # args: {userId:String, date:String, start:String}
    def delete(self):
        userId = request.form['userId']
        date = request.form['date']
        start = request.form['start']

        return jsonify(ToDoList.deleteTask(userId, date, start))
        
class DateController(Resource):
    
    # args: {userId:String, date:String}
    def delete(self):
        userId = request.form['userId']
        date = request.form['date']

        return jsonify(ToDoList.deleteDate(userId, date))