from flask import Flask, render_template
app=Flask(__name__)

@app.route('/home')
def hello_world():
  return(render_template('form.html')
  
if __name__ == '__main__':
  app.run()
