from flask_restful import Resource
from flask import request, jsonify

from model import ToDoList

class ListController(Resource):

    # params: {userId:String}
    def get(self,userId):
        return ToDoList.getList(userId)

    # args: {userId:String, date:String, start:String, task:String}  
    def post(self):
        userId = request.form['userId']
        date = request.form['date']
        start = request.form['start']
        task = request.form['task']

        ToDoList.createList(userId, date, start, task) 
        return jsonify(ToDoList.createList(userId, date, start, task))

    # args: {userId:String, date:String, start:String, task:String}
    def delete(self):
        userId = request.form['userId']
        date = request.form['date']
        start = request.form['start']
        task = request.form['task']

        return jsonify(ToDoList.deleteTask(userId, date, start, task))
        
    
 