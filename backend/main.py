from flask import Flask, jsonify, request
from flask_cors import CORS
from player import Player  # importa a classe
from task import Task  # importa a classe
from game import Game

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

game = Game(0)

@app.route('/players')
def get_players():
    return jsonify([p.to_dict() for p in players])

@app.route("/game",methods=['GET','POST'])
def game_status():
    global game
    if request.method == "GET":
        return jsonify({
            "state": game.get_state()
        })
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        game = Game(data["state"])
        print(game.get_state())
    return jsonify({
        "state": game.get_state()
    })

@app.route("/tasks",methods=['GET','POST'])
def game_status():
    if request.method == "GET":
        for task in tasks:
            return jsonify({
                "name": task.get_state(),
                "completed": task.get_state(),
                "place": task.get_state(),
                "objective": task.get_state()
            })
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        game = Game(data["state"])
        print(game.get_state())
    return jsonify({
        "state": game.get_state()
    })


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