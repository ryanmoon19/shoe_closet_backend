// REQUIREMENTS 
const express = require('express');
const app = express();
const mongoose = require('mongoose');

const Shoes = require('./models/shoes.js');

// MIDDLEWARE 
app.use(express.json());

// ROUTES

// create
app.post('/shoes', async (req, res) => {
    const createdShoes = await Shoes.create(req.body)
    res.json(createdShoes)
})

// MONGOOSE / MONGODB
mongoose.connect('mongodb://localhost:27017/merncrud')
mongoose.connection.once('open', ()=>{
    console.log('connection to mongoDB established...')
});

// LISTEN
app.listen(3000, ()=>{
    console.log('listening...')
}); 