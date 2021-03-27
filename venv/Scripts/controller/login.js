let app = angular.module('trabalho', []);
app.controller('login', function ($scope, $http) {

    $scope.login = "";
    $scope.senha = "";


    $scope.logar = function(){
        console.log("Logando kekw");
    }


}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});