let app = angular.module('trabalho', []);
app.controller('livros', function ($scope, $http, $window) {
    $scope.mostrarSide = false;

    $scope.livros = [
        {nome: "Dias Bons", descricao: "Um livro bonito", genero: "Romance"},
        {nome: "Dias Medio", descricao: "Um livro feio", genero: "Ação"},
        {nome: "Dias Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"}
    ];

    $scope.redirecionar = function(endereco){
        $window.location.href = endereco;
    }


}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});