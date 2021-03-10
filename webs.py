from flask import Flask
from threading import Thread
app=Flask('')
app = Flask(__name__)

@app.route('/') # this is the home page route

    
@app.route('/about')
def welcome():
  return "Booted"

 
   

@app.route('/')
def home():
   return ("ALL GOOD")
def run():
 app.run(host="0.0.0.0",port=8081)
def keep_alive():
 t=Thread(target=run)
 t.start()
 if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8081) # This line is required to run Flask on repl.it