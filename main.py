from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/hello',methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		firstname=request.form['firstname']
		return render_template('results.html',location=firstname)
	else:
		print "<h1>Hello</h1>"
	return render_template('form.html')

@app.route('/home')
def home():
	return render_template('index.html')
	
if __name__ == '__main__':
  app.run()
