const express = require('express');
const path = require('path');

const app = express();

// Serve static files from the dist directory
const angularDistFolder = path.join(__dirname, 'dist/bobcat-claws-app');
app.use(express.static(angularDistFolder));

// Handle all routes, ensuring they return the index.html file
app.get('*', (req, res) => {
    res.sendFile(path.join(angularDistFolder, 'index.html'));
});

// Set up the server to listen on all available network interfaces
const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running and accessible via http://147.26.102.120:${PORT}/`);
});

