var express = require('express');
var router = express.Router();
var os = require('os');
var networkInterfaces = os.networkInterfaces();
var amqp = require('amqplib');

var ip = getLocalIP();

/* GET home page. */
router.get('/', async (req, res, next) => {

});


async function test() {
  var everything = 'everything';
  var results = 'results';


  var conn = await amqp.connect('amqp://localhost');
  var ch = await conn.createChannel();
  var everythingQueue = await ch.assertQueue(everything, {durable: false});
  everythingQueue.sendToQueue(everything, Buffer.from)


  amqp.connect('amqp://localhost', (err, conn) => {
    console.log('starting amqp')
    if (err != null) bail (err);

    var everything = 'everything';
    var results = 'results';

    publisher(conn, everything);
    var t = await consumer(conn, results);   
    console.log(t)
  })
}

function publisher(conn, queue) {
  conn.createChannel(on_open);

  function on_open(err, ch) {
    if (err != null) bail (err);
    ch.assertQueue(queue, {durable: false})
    ch.sendToQueue(queue, Buffer.from(ip))
  }
}

async function consumer(conn, queue) {
  conn.createChannel(on_open);
  
  function on_open(err, ch) {
    if (err != null) bail (err);

    ch.assertQueue(queue, {durable: false});
    ch.consume(queue, (msg) => {
      if (msg != null) {
        // console.log(msg.content.toString());
        ch.ack(msg);
        mess =  msg.content.toString();
      }
    }).then()

  }
  return mess;
}

function getLocalIP() {
  return networkInterfaces['en1'][1].address;
}

function bail(err) {
  console.error(err);
  // process.exit(1);
}

module.exports = router;
