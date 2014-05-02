var BBBAdminControllers = angular.module('BBBAdminControllers', []);

BBBAdminControllers.controller('SystemUnameCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('/api/system/uname').success(function(data) {
      $scope.systemInfo = data;
    });
  }]);

BBBAdminControllers.controller('NetIfacesCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('/api/system/network').success(function(data) {
      $scope.network = data;
    });
  }]);
