def route(app):
    @app.route('/a')
    def hello_world():
        return "<p>Hello, World1asdsa</p>"
