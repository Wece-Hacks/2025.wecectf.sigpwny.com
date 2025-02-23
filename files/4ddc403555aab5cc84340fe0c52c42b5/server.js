const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const bot = require('./bot');

app.use(express.static(__dirname + '/public'));
app.use(express.json());

const flag = process.env.FLAG || "wecehacksctf{FAKE_FLAG}";

app.post('/api/submit', async (req, res) => {
    const { message } = req.body;
    if (!message) return res.status(400).send("Missing message field");

    const url = `http://localhost:${port}/posts?message=${encodeURIComponent(message)}`;
    const saw_popup = await bot.admin(url);

    if (saw_popup) {
        return res.send(flag);
    }
    
    res.send(`I didn't get any alerts.`);
})

app.listen(port, () => console.log(`Listening at http://localhost:${port}`))