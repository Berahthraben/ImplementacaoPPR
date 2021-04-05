let app = angular.module('trabalho', []);
app.controller('biblioteca', function ($scope, $http, $window) {
    $scope.mostrarSide = false;

    // $scope.livros = [
    //     {nome: "Dias Bons", descricao: "Um livro bonito", genero: "Romance"},
    //     {nome: "Dias Medio", descricao: "Um livro feio", genero: "Ação"},
    //     {nome: "Dias Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"},
    //     {nome: "Noites Boas", descricao: "Um livro chato", genero: "Política"},
    //     {nome: "Noites Ruins", descricao: "Um livro auto-confiante", genero: "Aventura"},
    //     {nome: "Noites Medias", descricao: "Um livro chato", genero: "Política"}
    // ];

    $scope.livros = [];

    $http.get('/livro').then((response) => {
        if(!(angular.equals(response.data, {}))) {
            $scope.livros = $scope.ajeitaLivros(response.data);
        }
    }, () => {
        $scope.msg = 'Ocorreu um erro. Isso pode ocorrer por causa dos arquivos. Tente novamente!'
    });


    $scope.ajeitaLivros = function(livros){
        let temp = [];
        let aux = 0;
        for(let i=0; i<livros.length; i+=2){
            if(!temp[aux]){
                temp.push({nome1: "", descricao1: "", genero1: "", nome2: "", descricao2: "", genero2: ""});
            }
            temp[aux].nome1 = livros[i].titulo;
            temp[aux].descricao1 = livros[i].descricao;
            temp[aux].genero1 = livros[i].genero;
            if(livros[i+1]){
                temp[aux].nome2 = livros[i+1].titulo;
                temp[aux].descricao2 = livros[i+1].descricao;
                temp[aux].genero2 = livros[i+1].genero;
            }
            aux++;
        }
        return temp;
    };

    $scope.redirecionar = function(endereco){
        $window.location.href = endereco;
    }


}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});