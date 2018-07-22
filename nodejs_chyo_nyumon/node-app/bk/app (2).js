const http = require('http');
const fs = require('fs');
const ejs = require('ejs');
// const url = require('url');

const index_page = fs.readFileSync('./index.ejs','utf8');

var server = http.createServer(getFromClient);
server.listen(3000);
console.log('server start');


function getFromClient(request,response) {
    fs.readFile('./index.html', 'UTF-8', 
        (error, data) => {
            var content = data.replace(/dummy_title/g,'タイトルです').replace(/dummy_content/g,'これがコンテンツです');
            response.writeHead(200, { 'Content-Type': 'text/html' });
            response.write(content);
            response.end();
        }
    );
}
