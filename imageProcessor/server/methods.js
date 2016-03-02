
var exec = Npm.require("child_process").exec;
Meteor.methods({
    process: function(img){
        //process
        exec('dir', function (error, stdout, stderr) {
            console.log(error);
            console.log(stdout);
        });
        console.log(img);
    }
})
