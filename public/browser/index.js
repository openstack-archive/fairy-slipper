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
    snapRemoteProvider.globalOptions = {
      disable: 'right',
      maxPosition: 235,
      minPosition: -235
    };

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

  .controller('MenuCtrl', ['$scope', '$location', '$routeParams', '$timeout', 'APIs', 'snapRemote', function($scope, $location, $routeParams, $timeout, APIs, snapRemote) {
    if ($location.path().indexOf('/by-path/') == 0) {
      $scope.filterByModel = 'by-path';
    } else if ($location.path().indexOf('/by-tag/') == 0) {
      $scope.filterByModel = 'by-tag';
    } else {
      $scope.filterByModel = 'by-path';
    }

    // only show sidebar after hovering for 2 seconds
    var timer;
    $scope.showSidebar = function () {
      timer = $timeout(function () {
        snapRemote.open('left');
      }, 500);
    };
    $scope.hideSidebar = function () {
      $timeout.cancel(timer);
    };

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
