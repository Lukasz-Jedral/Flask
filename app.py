from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/mypage/me',methods=['GET'])
def me():
    return render_template("me.html")


@app.route('/mypage/contact', methods=['GET','POST'])
def contact():
   if request.method == 'GET':
       return render_template("contact.html")

   elif request.method == 'POST':
        message = request.form['message']
        return message
