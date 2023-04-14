from flask_restful import Api
from controller import ListController

def router(app):
    route = Api(app)

    route.add_resource(ListController.ListController, '/delete-task', endpoint="delete-task")
    route.add_resource(ListController.ListController, '/', endpoint="list")
    route.add_resource(ListController.ListController, '/get-list/<string:userId>', endpoint="list-slug")