from pymodm import MongoModel, EmbeddedMongoModel, fields
from pymodm.connection import connect
from pymodm.errors import DoesNotExist

try:
    connect("mongodb://localhost:27017/chatBot")
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


def createList(userId, date, start, taskName):

    try:
        user = ToDoList.objects.get({"_id": userId})

        task = Task(start=start, task=taskName)
        try:
            listElement = next(filter(lambda x: x.date == date, user.list))
            listElement.tasks.append(task)
            user.save()
            return "created new task"
        except StopIteration:
            newDate = List(date=date, tasks=[task])
            user.list.append(newDate)
            user.save()
            return "created new date and task"
    except DoesNotExist:
        task = Task(start=start, task=taskName)
        list = List(date=date, tasks=[task])

        try:   
            ToDoList(userId=userId, list = [list]).save()
            return "created new todo list for new user"
        except Exception as e:
            print(e)
            return(e)




def deleteTask(userId, date, start, taskName):
    try:
        user = ToDoList.objects.get({"_id": userId})


        list_element = next(filter(lambda x: x.date == date, user.list), None)
      
        if list_element:
            task = next(filter(lambda x: x.start == start and x.task == taskName, list_element.tasks), None)
            if task:
                list_element.tasks.remove(task)
                
                if not list_element.tasks:
                    user.list.remove(list_element)
                    user.save()
                    return "deleted date"
                else:
                    user.save()
                    return "deleted task"
            else:
                return ("No task found")
        else:
            print("No date found")
    except DoesNotExist:
        print("todo list not existed")


def getList(userId):
    lists = ToDoList.objects.get({'_id': userId})
    print(lists.to_son()['list'])