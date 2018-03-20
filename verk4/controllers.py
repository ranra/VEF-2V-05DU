from verk4 import app
from verk4 import models as model
from flask import render_template



@app.route('/')
@app.route('/index')
def k():
    actorList = model.actorList

    return render_template('forsida.html', actorList = actorList)


#
# @app.route("/book/<bookNUM>")
# def book(bookNUM):
#     print(int(bookNUM))
#     bok = model.booklist[int(bookNUM)] # Þarf að útfæra betur
#     return render_template('leikarar.html', bok = bok)