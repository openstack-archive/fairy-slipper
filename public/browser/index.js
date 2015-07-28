'use strict';

angular.module('fairySlipper.index', [
  'ngRoute',
  'ngResource',
  'snap'
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

  .controller('MenuCtrl', ['$scope', '$location', '$routeParams', 'APIs', 'snapRemote', function($scope, $location, $routeParams, APIs, snapRemote) {
    if ($location.path().indexOf('/by-path/') == 0) {
      $scope.filterByModel = 'by-path';
    } else if ($location.path().indexOf('/by-tag/') == 0) {
      $scope.filterByModel = 'by-tag';
    } else {
      $scope.filterByModel = 'by-path';
    }

    $scope.snapRemote = snapRemote;
    $scope.$routeParams = $routeParams;

    APIs.query().$promise.then(function (data) {
      $scope.services = {};
      angular.forEach(data, function (value) {
        var service = value['service'];
        if (!$scope.services[service]) {
          $scope.services[service] = {
            apis: [],
            title: value['title']};
        }
        $scope.services[service]['apis'].push(value);
        });
    });

  }]);
