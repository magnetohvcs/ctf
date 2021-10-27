from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return """<html>
   <body>
      <form action = "upload" method = "POST"
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>"""

@app.route('/upload', methods = [ 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8888)