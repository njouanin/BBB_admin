var BBBAdminApp = angular.module('BBBAdminApp', [
  'ngRoute',
  'BBBAdminControllers'
]);

BBBAdminApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.when('/system', {templateUrl: '/ng-app/partials/system.html'});
    $routeProvider.when('/board', {templateUrl: '/ng-app/partials/board.html',controller: 'BoardCtrl'});
    $routeProvider.otherwise({redirectTo: '/system'});
  }]);