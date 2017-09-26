const express = require('express')
const app = express()
const logfmt = require('logfmt')

app.use(logfmt.requestLogger());

app.get('/', function (req, res) {
	res.send('Hello');
})

app.listen(3000, function(){
	console.log('Port:3000');
})
