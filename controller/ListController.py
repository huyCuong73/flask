from flask_restful import Resource
from flask import request, jsonify
import json
from model import ToDoList

class ListController(Resource):

    # params: {userId:String}
    def get(self,userId):
        return jsonify(ToDoList.getList(userId))

    # args: {userId:String, date:String, start:String, task:String}  
    def post(self):
        data = request.json
        data_dict = json.loads(data)
        userId = data_dict['userId']
        date = data_dict['date']
        start = data_dict['start']
        task = data_dict['task']

        return jsonify(ToDoList.createTask(userId, date, start, task))
    
    # args: {userId:String, date:String, start:String}
    def delete(self):
        data = request.json
        data_dict = json.loads(data)
        userId = data_dict['userId']
        date = data_dict['date']
        start = data_dict['start']

        return jsonify(ToDoList.deleteTask(userId, date, start))
        
class DateController(Resource):
    
    # args: {userId:String, date:String}
    def delete(self):
        data = request.json
        data_dict = json.loads(data)
        userId = data_dict['userId']
        date = data_dict['date']

        return jsonify(ToDoList.deleteDate(userId, date))