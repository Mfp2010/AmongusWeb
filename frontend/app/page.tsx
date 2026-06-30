'use client'

import { useEffect, useState } from "react";

export default function Home() {
  // Criamos os estados para a mensagem e para a lista de jogadores
  const [msg, setMsg] = useState<string | null>(null);
  const [players, setPlayers] = useState<string[]>([]);
  const [tasks, setTasks] = useState<string[]>([]);
  const [game, setGame] = useState<string[]>([]);
  const [imposters, setImposters] = useState<string[]>([]);

  useEffect(() => {
    // Função que faz o pedido ao backend
    const fetchData = () => {
      fetch("http://localhost:5000/")
        .then(r => {
          if (!r.ok) throw new Error("Erro na API");
          return r.json();
        })
        .then(data => {
          setMsg(data.msg); // Atualiza a lista com o que veio do backend
        })
        .catch(err => console.error("Erro ao procurar dados (main page):", err));
      fetch("http://localhost:5000/players")
        .then(r => {
          if (!r.ok) throw new Error("Erro na API");
          return r.json();
        })
        .then(data => {
          setPlayers(data); // Atualiza a lista com os players que vieram do backend
        })
        .catch(err => console.error("Erro ao procurar dados (/players):", err));
      fetch("http://localhost:5000/tasks")
        .then(r => {
          if (!r.ok) throw new Error("Erro na API");
          return r.json();
        })
        .then(data => {
          setTasks(data.tasks); // Atualiza a lista com as tasks que vieram do backend
        })
        .catch(err => console.error("Erro ao procurar dados (/tasks):", err));
        fetch("http://localhost:5000/get_game")
        .then(r => {
          if (!r.ok) throw new Error("Erro na API");
          return r.json();
        })
        .then(data => {
          setImposters(data.imposters); // Atualiza a lista com o jogo que veio do backend
        })
        .catch(err => console.error("Erro ao procurar dados (/get_game):", err));
    };

    // Executa imediatamente ao carregar a página
    fetchData();

    // Faz o Polling: Executa a função a cada 3 segundos (3000ms)
    const interval = setInterval(fetchData, 3000);

    // Limpa o intervalo quando o componente deixa de existir (evita fugas de memória)
    return () => clearInterval(interval);
  }, []);

  return (
    <main style={{ padding: '20px' }}>
      <h2>{msg ?? "A carregar..."}</h2> 
      
      <h3>Lista de Jogadores:</h3>
      {players.length === 0 ? (
        <p>Nenhum jogador conectado.</p>
      ) : (
        <><table>
          <tr>
            <th>Jogador</th>
            <th>Impostor?</th>
            <th>Cooldown</th>
            <th>Morto</th>
            {tasks.map((task, index) => (<th>{task.name} {task.place}</th>))}
          </tr>
          {players.map((player, index) => (<tr>
            <td>{player.name}</td>
            <td>Não</td>
            <td>-</td>
            <td>{player.state ? "Morto" : "Vivo"}</td>
            {player.tasks.map((task, index) => (<td>{task.completed ? "✓" : "✗"}</td>))}
          </tr>))}
          {imposters.map((imposter, index) => (<tr>
            <td>{imposter.player.name}</td>
            <td>Sim</td>
            <td>{imposter.cooldown ? "Sim" : "Não"}</td>
            <td>{imposter.player.state ? "Morto" : "Vivo"}</td>
            {tasks.map((task, index) => (<td>-</td>))}
          </tr>))}
        </table></>
      )}
    </main>
  );
}