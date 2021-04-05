let app = angular.module('trabalho', []);
app.controller('login', function ($scope, $http, $window) {

    $scope.login = "";
    $scope.senha = "";
    $scope.loginIncorreto = false;


    $scope.logar = function(){
        let send = {"email": $scope.login, "senha": $scope.senha};
        $http.post('/login', send).then((response) => {
            if(angular.equals(response.data, {})){
                $scope.loginIncorreto = true;
            }else{
                $window.location.href = '/biblioteca';
            }
        }, () => {
            $scope.msg = 'Ocorreu um erro. Isso pode ocorrer por causa dos arquivos. Tente novamente!'
        });
    }


}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});