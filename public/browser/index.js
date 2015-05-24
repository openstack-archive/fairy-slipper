'use strict';

angular.module('fairySlipper.index', [
  'ngRoute',
  'ngResource',
  'swaggerUi'
])
  .config(['$routeProvider', 'snapRemoteProvider', function($routeProvider, snapRemoteProvider) {
    $routeProvider.when('/', {
      templateUrl: 'browser/index.html',
      controller: 'IndexCtrl'
    });
    snapRemoteProvider.globalOptions.disable = 'right';
  }])

  .controller('IndexCtrl', ['$scope', '$http', function($scope, $http) {

  }])

  .factory('APIs', ['$resource', function($resource) {
    return $resource('/doc', {
    }, {
    }, {
      stripTrailingSlashes: false
    });
  }])

  .controller('MenuCtrl', ['$scope', 'APIs', function($scope, APIs) {
    APIs.get().$promise.then(function (data) {
      $scope.services = {};
      angular.forEach(data, function (value, key) {
        if (key != '$promise' && key != '$resolved') {
          var service = value['service'];
          if (!$scope.services[service]) {
            $scope.services[service] = {
              apis: [],
              title: value['title']};
          }
          value.url = key;
          $scope.services[service]['apis'].push(value);
        }});
    });
  }]);
