'use strict';

angular.module('fairySlipper', [
  'ngRoute',
  'snap',
  'fairySlipper.browser',
  'fairySlipper.index'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/'});
}]);
