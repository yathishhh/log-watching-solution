// document.addEventListener('DOMContentLoaded', function() {
//     const socket = io.connect('http://' + document.domain + ':' + location.port);
//     const logContainer = document.getElementById('log-container');

//     
//     socket.on('log_update', function(msg) {
//         const logEntry = document.createElement('div');
//         logEntry.textContent = msg.data;
//         logContainer.appendChild(logEntry);
//     });
// });
document.addEventListener('DOMContentLoaded', function() {
    const socket = io.connect(window.location.origin);
    const logContainer = document.getElementById('log-container');

    
    socket.on('log_update', function(msg) {
        const logEntry = document.createElement('div');
        logEntry.textContent = msg.data;
        logContainer.appendChild(logEntry);
    });
});
