from pyramid.view import view_config
import gevent

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'MyProject'}

from socketio.namespace import BaseNamespace
class ChatNamespace(BaseNamespace):
    def initialize(self):
        print "INIT"
    def on_log(self, data):
        print(data)
        self.emit("Hi")
    def on_count(self, data):
        for x in range (0, int(data)):
            self.emit("count_response", {"value": x})
            gevent.sleep(0.1)

@view_config(route_name='socketio')
def socketio(request):
    from socketio import socketio_manage
    socketio_manage(request.environ,
                    {"/chat": ChatNamespace},
                    request=request)
