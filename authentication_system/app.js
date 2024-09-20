const express = require('express');
const dotenv = require('dotenv');
const sequelize = require('./config/db');
const authRoutes = require('./routes/authRoutes');

dotenv.config();

const app = express();

app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);

app.get('/health', (req, res) => {
    res.status(200).send('OK');
});

// Database sync and start server
sequelize.sync().then(() => {
    app.listen(6000, () => {
        console.log('Server is running on port 6000');
    });
}).catch(error => {
    console.error('Unable to connect to the database:', error);
});
