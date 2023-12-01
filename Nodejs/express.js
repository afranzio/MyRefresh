const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send(process.env);
});

app.get("/get", (req, res) => {
    res.send("Jerry Bottom");
});

app.listen(3000);
