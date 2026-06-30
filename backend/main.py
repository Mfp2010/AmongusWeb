from flask import Flask, jsonify
from flask_cors import CORS
from player import Player  # importa a classe
from task import Task  # importa a classe

app = Flask(__name__)
CORS(app)

tasks = [
    Task("task1",0,"eletrica","fios"),
    Task("task2",1,"1.09","gambling"),
    Task("task3",1,"cesium","rubix cube"),
    Task("task4",0,"auditorio","matematica")

]

players = [
    Player("Joao",tasks , 0),
    Player("Maria", tasks, 1),
]

@app.route('/players')
def get_players():
    return jsonify([p.to_dict() for p in players])

@app.route('/tasks')
def get_tasks():
    return jsonify([t.to_dict() for t in tasks])


@app.route("/")
def hello_world():
    # Juntamos o msg e os players num único JSON
    return jsonify({
        "msg": "Hello, World!",
        "players": [p.to_dict() for p in players],
        "tasks": [t.to_dict() for t in tasks]
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)