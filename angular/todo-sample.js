angular.module("tsm", [])
.controller("tsc" , function(){
    var tsv = this;
    tsv.names=['sarath','chandra'];
    tsv.add= function(){
        tsv.names.push(tsv.tobeadded);
    }
});