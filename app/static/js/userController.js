var user_url = "api/users"
var app = angular.module('myApp', [])
app.controller('userCtrl', function($scope, $http) {
    $http.get(user_url).then(function(response) {
        $scope.users = angular.fromJson(response.data).users
    })
})

var login_url = 'login'
app.controller('loginCtl', function($scope, $http, $window) {
    $scope.login = function(email, password) {
        var data = {
            "email": email,
            "password": password
        }

        $http.post(login_url, data)
            .then(function(response) {
                alert(response.status)
                $window.location.href = '/index'
            })
    }
})