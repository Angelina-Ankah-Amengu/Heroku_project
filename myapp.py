from flask import Flask , render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello world'
    
@app.route('/h')
def in_html():
    return '<html><head><body><h1 style="text-align:center;">ClassBook2018</h1><div class="profile"><hr>Students Profile</hr></div><div class="student_info"></div></body></head></html>'
    
@app.route('/whereami')
def whereami():
    return 'Koforidua!'
    
   
@app.route('/homepage')
def homepage():
	title = "Global Code 2018"
	paragraph = ["hi there"]
	return render_template('index1.html', title=title, paragraph=paragraph)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

