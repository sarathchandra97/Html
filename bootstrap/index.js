var convert = require('xml-js');
var result1 = convert.xml2json(xml, {compact: true, spaces: 4});    
var result2 = convert.xml2json(xml, {compact: false, spaces: 4});
var obj = JSON.parse(result1)
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
url = "http://jiofi.local.html/st_dev.w.xml"
function console_print(response_string){
    var result1 = convert.xml2json(response_string, {compact: true, spaces: 4}); 
    var response_json = JSON.parse(result1)
    console.log(response_json['dev']['batt_per']['_text'])   
    return response_json['dev']['batt_per']['_text']
}
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            return callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}
function getBatteryStatus(){
    return httpGetAsync(url,console_print);
}
getBatteryStatus()
// TODO
/*
    Organize these things
    1. asynchronous calling and extracting the response
    3. checking the respose wheather it is connected or not
    2. convert to json 
    3. extract battery percent from the json
    4. pass it the model
    Extensions to this thing 
    5. getting how many members can connect and how are connecct
    6. go the whitelist and back list here if possible
    7. 
*/