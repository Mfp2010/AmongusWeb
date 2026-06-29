'use client'

import { useEffect, useState } from "react";

export default function Home() {
  // Criamos os estados para a mensagem e para a lista de jogadores
  const [msg, setMsg] = useState<string | null>(null);
  const [players, setPlayers] = useState<string[]>([]);

  useEffect(() => {
    // Função que faz o pedido ao backend
    const fetchData = () => {
      fetch("http://localhost:5000/")
        .then(r => {
          if (!r.ok) throw new Error("Erro na API");
          return r.json();
        })
        .then(data => {
          setMsg(data.msg);
          setPlayers(data.players); // Atualiza a lista com o que veio do backend
        })
        .catch(err => console.error("Erro ao procurar dados:", err));
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
        <ul>
          {players.map((player, index) => (
            <li key={index}>{player}</li>
          ))}
        </ul>
      )}
    </main>
  );
}