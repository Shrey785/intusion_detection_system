document.getElementById('checkBtn').addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/alerts');
        const alerts = await response.json();

        const tbody = document.querySelector('#alertsTable tbody');
        tbody.innerHTML = ''; // Clear previous alerts

        alerts.forEach(alert => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${alert.time}</td>
                <td>${alert.type}</td>
                <td class="severity-${alert.severity.toLowerCase()}">${alert.severity}</td>
                <td>${alert.source}</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Failed to fetch alerts:', error);
    }
});
