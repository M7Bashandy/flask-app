from flask import Flask, request,render_template
import MySQLdb
import dataBaseOP
app = Flask(__name__)

@app.route('/' ,methods=['GET' ,'POST'])
def view():
    nodes,item=dataBaseOP.Table()

    if request.method=='POST':
        name=request.form["nodeName"]
        Parent=request.form["Parent"]
        Child=request.form["Child"]

        dataBaseOP.register(name,"")
        if Parent != "":
            id, node_name, PID = dataBaseOP.Query(str(Parent))
            dataBaseOP.update(name, id)
        if Child != "":
            id, node_name, PID = dataBaseOP.Query(str(name))
            dataBaseOP.update(Child, id)
        nodes, item = dataBaseOP.Table()
        return render_template('Table.html',options=item)

    return render_template('index.html',options=nodes)


@app.route('/parentsOf')
def Parent():
    response = []
    node = request.args.get('node')
    response=dataBaseOP.parent(str(node))
    return str(response)


@app.route('/childrenOf')
def Child():

    response=[]
    node = request.args.get('node')
    result=dataBaseOP.child(str(node))
    return str(result)

if __name__ == '__main__':
    app.run()
