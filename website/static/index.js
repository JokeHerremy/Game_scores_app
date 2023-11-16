function deleteGame(gameId) {
  fetch("/delete-game", {
    method: "POST",
    body: JSON.stringify({ gameId: gameId }),
  }).then((_res) => {
    window.location.href = "/game_entries";
  });
}
function deletePlayer(playerId) {
  fetch("/delete-player", {
    method: "POST",
    body: JSON.stringify({ playerId: playerId }),
  }).then((_res) => {
    window.location.href = "/player_entries";
  });
}
