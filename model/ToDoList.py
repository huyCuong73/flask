from pymodm import MongoModel, EmbeddedMongoModel, fields
from pymongo.write_concern import WriteConcern
from pymodm.connection import connect
from pymodm.errors import DoesNotExist

try:
    connect("mongodb+srv://toanta1006:123456Aa@todolist.iboamwh.mongodb.net/chatBot?retryWrites=true&w=majority", alias="my-app")
except Exception as e:
    print(e)

class Task(EmbeddedMongoModel):
    start = fields.CharField()
    task = fields.CharField()

class List(EmbeddedMongoModel):
    date = fields.CharField()
    tasks = fields.EmbeddedDocumentListField(Task, blank = True)

class ToDoList(MongoModel):
    userId = fields.CharField(primary_key=True)
    list = fields.EmbeddedDocumentListField(List, blank = True)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
        collection_name = 'TodoList'


def createTask(userId, date, start, taskName):

    try:
        user = ToDoList.objects.get({"_id": userId})
        
        task = Task(start=start, task=taskName)
        try:
            listElement = next(filter(lambda x: x.date == date, user.list))
            task = next(filter(lambda x: x.start == start, listElement.tasks))
            if task:
                return {"status":"409","msg":"task already existed"}
            else:
                listElement.tasks.append(task)
                user.save()
            return {"status":"200","msg":"created new task"}
        except StopIteration:
            newDate = List(date=date, tasks=[task])
            user.list.append(newDate)
            user.save()
            return {"status":"201","msg":"created new date and task"}
    except DoesNotExist:
        task = Task(start=start, task=taskName)
        list = List(date=date, tasks=[task])

        try:   
            ToDoList(userId=userId, list = [list]).save()
            return {"status":"202","msg":"created new todo list for new user"}
        except Exception as e:
            print(e)
            return(e)




def deleteTask(userId, date, start):
    try:
        user = ToDoList.objects.get({"_id": userId})


        listElement = next(filter(lambda x: x.date == date, user.list), None)
      
        if listElement:
            task = next(filter(lambda x: x.start == start, listElement.tasks), None)
            if task:
                listElement.tasks.remove(task)
                
                if not listElement.tasks:
                    user.list.remove(listElement)
                    user.save()
                    return {"status": "200", "msg": "deleted date"}
                else:
                    user.save()
                    return {"status": "200", "msg": "deleted task"}
            else:
                return {"status": "404", "msg": "no task found"}
        else:
            return {"satus":"405","msg":"No date found"}
    except DoesNotExist:
        return {"status":"406","msg":"todo list not existed"}


def getList(userId):
    todoList = ToDoList.objects.get({'_id': userId})
    
    if (len(todoList.to_son()['list']) == 0):
        return {"status":"404", "msg":"todo list empty"}
    else:
        return todoList.to_son()['list']


def deleteDate(userId, date):

    todoList= ToDoList.objects.get({"_id": userId})
    listElement = next(filter(lambda x: x.date == date, todoList.list), None)
    if listElement:
        todoList.list.remove(listElement)
        todoList.save()
        return {"code":"200","msg": "deleted date"}
    else:
        return {"code":"404","msg": "date not found"}