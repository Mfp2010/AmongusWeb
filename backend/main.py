from flask import Flask, jsonify, request
from flask_cors import CORS
from player import Player  # importa a classe
from task import Task  # importa a classe
from game import Game
from impostors import Impostor

app = Flask(__name__)
CORS(app)

emergency_meeting = False

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

imposters = [Impostor(Player("Abel",tasks,0),0)]

game = Game(0, players, imposters)

@app.route('/players')
def get_players():
    return jsonify([p.to_dict() for p in players])

@app.route('/get_game')
def get_game():
    return jsonify(game.to_dict())

@app.route('/kill',methods=['POST'])
def kill_player():
    global game
    data = request.get_json()
    players[data["player"]].set_state(1)
    imposters[data["imposter"]].set_cooldown(1)
    game.set_players(players)
    game.set_imposters(imposters)
    return jsonify({"players": players, "imposters": imposters})

@app.route("/vote",methods=['POST'])
def vote():
    global game
    data = request.get_json()
    if data["result"] == "player":
        players[data["id"]].set_state(1)
    elif data["result"] == "imposter":
        imposters[data["id"].set_state(1)]
    else:
        game.set_state(1)

@app.route("/game",methods=['GET','POST'])
def game_status():
    global game
    if request.method == "GET":
        return jsonify({
            "state": game.get_state(),
            "emergency_meeting": emergency_meeting
        })
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        game = Game(data["state"], data["players"], data["imposters"])
        print(game.get_state())
    return jsonify({
        "state": game.get_state(),
        "emergency_meeting": emergency_meeting
    })

@app.route("/set_cooldown",methods=['POST'])
def set_cooldown():
    global game
    data = request.get_json()
    print(data)
    imposters = game.get_imposters()
    print([i.to_dict() for i in imposters])
    imposters[data["imposter"]].set_cooldown(data["cooldown"])
    print([i.to_dict() for i in imposters])
    game.set_imposters(imposters)
    return jsonify({
        "imposters": [i.to_dict() for i in imposters]
    })

@app.route("/tasks",methods=['GET','POST'])
def tasks_status():
    if request.method == "GET":
        print(tasks[0].get_name())
        return jsonify({
        "tasks": [t.to_dict() for t in tasks],
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