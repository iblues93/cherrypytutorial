"""
Start this server!

Access it at localhost:8080/index
"""

import cherrypy, base64, os

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
            <p>Upload your file!</p> 
            <form method="post" enctype="multipart/form-data" action="upload">
              <input type="file" name="myFile" />
              <button type="submit">Send your file name!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def upload(self, myFile):
        out = """<html>
        <body>
            myFile length: %s<br />
            myFile filename: %s<br />
            myFile mime-type: %s
        </body>
        </html>"""

        # Although this just counts the file length, it demonstrates
        # how to read large files in chunks instead of all at once.
        # CherryPy reads the uploaded file into a temporary file;
        # myFile.file.read reads from that.
        with open("uploads/html_upload.jpg",'wb') as f:
            size = 0
            while True:
                data = myFile.file.read(8192)
                if not data:
                    break
                f.write(data)
                size += len(data)

        return out % (size, myFile.filename, myFile.content_type)
    
    @cherrypy.expose
    def echo_file_name(self, filepath):
        return "The file path you entered is : {}".format(filepath)

    @cherrypy.expose
    def get_img(self, filename, data):
        with open("uploads/{}".format(filename),'wb') as f:
            f.write(base64.b64decode(data))
        return "{} received.".format(filename)

if __name__ == '__main__':
    cherrypy.quickstart(FileNameReceiver())