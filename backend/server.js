const express = require('express')
//express app
const app = express()
const data = require('./routes/data')
//middleware
app.use(express.json())

app.use('/api/')