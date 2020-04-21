from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    pics = open("links.txt", "r", encoding="utf-8")
    pics_list = [row for row in pics]
    pics.close()
    return render_template('index.html', pics_list=pics_list)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add-pic", methods=["POST"])
def add_pic():
    description = request.form.get("description")
    pic = request.form.get["pic"]
    pics = open('links.txt', 'a+', encoding="utf-8")
    pics.write(pic + "\n" + description)
    ururu = [row.split[0] for row.split() in pics if row]
    pics.close()
    return render_template("picadded.html")

