from flask import render_template, Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/JSONView/')
def helloXML():
    return render_template('JSONHello.html')

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8080, debug=True)
