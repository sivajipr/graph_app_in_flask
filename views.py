from flask import Flask, render_template,flash,redirect,url_for,request,jsonify
import json
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')
@app.route('/colour',methods=['POST','GET'])
def colour():
	vertexes=request.form['vertex']
	vertexes=json.loads(vertexes)
	colours=["blue","green","yellow","orange","red"]
	cond=False
	for vertex in vertexes:
		ac=find(vertex['name'],vertexes)
		i=0
		cond=False
		while cond==False and i<len(colours):
			if colours[i] in ac:
				cond=False
				i=i+1
			else:
				cond=True
				vertex['color']=colours[i]
	return jsonify({1:vertexes})
def find(name,vertexes):
	vlist=[]
	for vertex in vertexes:
		if name in vertex['adjacent']:
			vlist.append(vertex['color'])
	return vlist
if __name__ == '__main__':
 app.run(debug=True)
