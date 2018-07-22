const http = require('http');
const fs = require('fs');
const ejs = require('ejs');
const url = require('url');

const index_page = fs.readFileSync('./index.ejs', 'utf8');
const style_css = fs.readFileSync('./style.css', 'utf8');

var server = http.createServer(getFromClient);
server.listen(3000);
console.log('server start');


function getFromClient(request, response) {
    var content = ejs.render(index_page,{
        title:"Indexページ",
        content:"これはテンプレート使ってます"
    });
    response.writeHead(200, { 'Content-Type': 'text/html' });
    response.write(content);
    response.end();
}
