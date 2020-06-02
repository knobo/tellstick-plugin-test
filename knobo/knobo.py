import cherrypy
import os.path
from base import Plugin, implements
from telldus.web import IWebReactHandler

current_dir = os.path.dirname(os.path.abspath(__file__))
conf = { 
    '/knobo': {'tools.staticdir.on': True,
              'tools.staticdir.dir': os.path.join(current_dir, 'public'),
              'tools.staticdir.content_types': {'rss': 'application/xml',
                                                'atom': 'application/atom+xml'}}}

class PlugMe (object):
    """The pluginomunter"""
    def init():
        cherrypy.tree.mount(Knobo(), '/blog', blog_conf)

class Knobo (Plugin):
    implements(IWebReactHandler)

    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @staticmethod
    def main():
        print("The main");


def main():    
    cherrypy.quickstart(Knobo(), '/', config=conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8081,
})

        
if __name__ == "__main__":
    main()

