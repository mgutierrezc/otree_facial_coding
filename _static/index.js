const files = require('fs');
files.writeFile("/tmp/test", "Hey there!", function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
}); 