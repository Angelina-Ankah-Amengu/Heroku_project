from flask import Flask , render_template
 
app = Flask(__name__)
 

   
@app.route('/homepage')
def homepage():
	title = "Global Code 2018"
	paragraph = ["hi there"]
	return render_template('index1.html', title=title, paragraph=paragraph)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

