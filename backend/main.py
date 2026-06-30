from flask import Flask, jsonify
from flask_cors import CORS
from player import Player  # importa a classe
from task import Task  # importa a classe

app = Flask(__name__)
CORS(app)

tasks = [
    Task("task1",0),
    Task("task2",1),
    Task("task3",1),
    Task("task4",0)

]

players = [
    Player("Joao",tasks , 0),
    Player("Maria", tasks, 1),
]

@app.route('/players')
def get_players():
    return jsonify([p.to_dict() for p in players])



@app.route("/")
def hello_world():
    # Juntamos o msg e os players num único JSON
    return jsonify({
        "msg": "Hello, World!",
        "players": players,
        "tasks": tasks
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)