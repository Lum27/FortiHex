async function loadChallenges() {
  const res = await fetch('http://localhost:5000/challenges');
  const data = await res.json();
  const container = document.getElementById('challenges');
  data.forEach(ch => {
    const div = document.createElement('div');
    div.innerHTML = `
      <h3>${ch.title}</h3>
      <p>${ch.description}</p>
      <input type="text" id="input-${ch.id}" placeholder="Enter solution">
      <button onclick="submit(${ch.id})">Submit</button>
      <hr>
    `;
    container.appendChild(div);
  });
}

async function submit(id) {
  const input = document.getElementById(`input-${id}`).value;
  const res = await fetch('http://localhost:5000/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ challenge_id: id, submission: input })
  });
  const data = await res.json();
  alert(data.message);
}

loadChallenges();
