let app = angular.module('trabalho', []);
app.controller('biblioteca', function ($scope, $http) {
    $scope.mostrarSide = false;

    $scope.livros = [
        {nome: "Dias Bons", descricao: "Um livro bonito", genero: "Romance"},
        {nome: "Dias Medio", descricao: "Um livro feio", genero: "Ação"},
        {nome: "Dias Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"},
        {nome: "Noites Boas", descricao: "Um livro chato", genero: "Política"},
        {nome: "Noites Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"},
        {nome: "Noites Medias", descricao: "Um livro chato", genero: "Política"}
    ];

    $scope.ajeitaLivros = function(){
        let temp = [];
        let aux = 0;
        for(let i=0; i<$scope.livros.length; i+=2){
            if(!temp[aux]){
                temp.push({nome1: "", descricao1: "", genero1: "", nome2: "", descricao2: "", genero2: ""});
            }
            temp[aux].nome1 = $scope.livros[i].nome;
            temp[aux].descricao1 = $scope.livros[i].descricao;
            temp[aux].genero1 = $scope.livros[i].genero;
            if($scope.livros[i+1]){
                temp[aux].nome2 = $scope.livros[i+1].nome;
                temp[aux].descricao2 = $scope.livros[i+1].descricao;
                temp[aux].genero2 = $scope.livros[i+1].genero;
            }
            aux++;
        }
        console.log(temp);
        return temp;
    };

    $scope.livros = $scope.ajeitaLivros();




}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});