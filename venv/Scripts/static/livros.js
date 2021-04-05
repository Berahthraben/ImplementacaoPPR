let app = angular.module('trabalho', []);
app.controller('livros', function ($scope, $http) {
    $scope.mostrarSide = false;

    $scope.livros = [
        {nome: "Dias Bons", descricao: "Um livro bonito", genero: "Romance"},
        {nome: "Dias Medio", descricao: "Um livro feio", genero: "Ação"},
        {nome: "Dias Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"}
    ];



}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});