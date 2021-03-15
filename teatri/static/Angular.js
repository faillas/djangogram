var sito=angular.module('myApp', [])

//cambio tema
sito.controller('Tema', function($scope) {
    $scope.count = 0;
	$scope.val = 0;
    $scope.tema = 'text-black bg-light';
    $scope.myFunction = function() {
        $scope.count++;
        if ($scope.count%2==0) {
            $scope.tema="text-black bg-light";
            // background-color: #f8f9fa;
            // color: #212529

        }else{
            $scope.tema="text-white bg-dark";
            // background-color: #212529;
            // color: #fff
        }
    }
});




