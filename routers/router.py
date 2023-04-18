from flask_restful import Api
from controller import ListController

def router(app):
    route = Api(app)

    route.add_resource(ListController.ListController, '/delete-task', endpoint="delete-task")
    route.add_resource(ListController.ListController, '/', endpoint="list")
    route.add_resource(ListController.ListController, '/get-list/<string:userId>', endpoint="get-list")
    route.add_resource(ListController.DateController, '/delete-date', endpoint="delete-date")
    route.add_resource(ListController.NotificationController, '/get-notification', endpoint="get-notification")