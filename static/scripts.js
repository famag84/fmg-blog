function checkPassword() {
    const password = document.getElementById('password').value;
    if (password === 'yourpassword') {  // Replace 'yourpassword' with the actual password
        document.getElementById('personal-content').style.display = 'block';
        loadCurveNames();
    } else {
        alert('Incorrect password');
    }
}

function loadCurveNames() {
    fetch('/get_curve_names')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('curve-name');
            data.forEach(name => {
                const option = document.createElement('option');
                option.value = name;
                option.textContent = name;
                select.appendChild(option);
            });
        });
}

function fetchCurve() {
    const curveName = document.getElementById('curve-name').value;
    fetch(`/fetch_curve?curve_name=${curveName}`)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('curve-chart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: curveName,
                        data: data.values,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
}
