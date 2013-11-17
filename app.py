from subprocess import Popen
import cherrypy

class Root(object):
    def index(self):
        Popen(['python', 'model.py'])
        return 'SUCCESS!'
    index.exposed = True

cherrypy.quickstart(Root())
