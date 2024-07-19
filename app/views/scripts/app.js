document.addEventListener('DOMContentLoaded', function () {
    fetchUsers();
    fetchFlights();
});

function fetchUsers() {
    fetch('/users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = '';
            data.forEach(user => {
                const li = document.createElement('li');
                li.textContent = `${user.name} (${user.email})`;
                userList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
}

function fetchFlights() {
    fetch('/flights')
        .then(response => response.json())
        .then(data => {
            const flightList = document.getElementById('flight-list');
            flightList.innerHTML = '';
            data.forEach(flight => {
                const li = document.createElement('li');
                li.textContent = `Flight ${flight.flight_number} to ${flight.destination} on ${flight.departure_date}`;
                flightList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching flights:', error));
}
