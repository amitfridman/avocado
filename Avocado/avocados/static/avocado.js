
var app = angular.module('myApp',[]).config(['$httpProvider', '$interpolateProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
}]);

app.controller('formCtrl', function($scope,$http) {
    $scope.forminput = {
        total_volume:0,
        t_4046:0,
        t_4225:0,
        t_4770:0,
        total_bags:0,
        small_bags:0,
        large_bags:0,
        x_large_bags:0,
        type: "conventional",
        year:2020,
        region: "Albany"
    } ;
    $scope.types = ["conventional","organic"];
    $scope.date = new Date();
    $scope.result = "pending";

    $scope.year = function(start) {
        var result = [];
        for (var i = start; i <= 2020; i++) {
            result.push(i);
        }
        return result;
    };

    $scope.submit = function(){

      $http.post("http://192.168.42.114:8443/avocado/",$scope.forminput)
          .then(function mySuccess(response) {
            $scope.data = response.data;
            $scope.result = response.statusText;
          }, function myError(response) {
            $scope.result = response.statusText;
            $scope.data = response.data;
          });
    };
   $scope.is_valid = function(result){
        return (result !== "OK");
   };
});
