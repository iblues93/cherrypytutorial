"""
Start this server!

Access it at localhost:8080/index
"""

import cherrypy

class FileNameReceiver(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="echo_file_name">
              <input type="file" name="filepath" />
              <button type="submit">Send your file name!</button>
            </form>
            <p>OR</p>
            <form method="get" action="echo_file_name">
              Enter your file path here : 
              <input type="text" name="filepath" />
              <button type="submit">Send your file name!</button>
            </form>
           
          </body>
        </html>"""

    @cherrypy.expose
    def echo_file_name(self, filepath):
        return "The file path you entered is : {}".format(filepath)

if __name__ == '__main__':
    cherrypy.quickstart(FileNameReceiver())