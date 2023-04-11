const mongoose = require('mongoose');

const shoesSchema = new mongoose.Schema({
    name: String,
    description: String,
});

const Shoes = mongoose.model('Shoe', shoesSchema);

module.exports = Shoes; 