const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from the backend!' });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
