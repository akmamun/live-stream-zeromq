from flask import Flask, render_template, Response
from stream import streamer

app = Flask(__name__)

def gen():

  while True:
      s = streamer()
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + s + b'\r\n\r\n')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/camera')
def camera():
  return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)