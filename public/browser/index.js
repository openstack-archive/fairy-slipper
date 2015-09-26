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

  .factory('navigation', ['APIs', function(APIs) {
    var nav_by_service = {};
    var extensions = [];
    var ends_with = function (string, substring) {
      return string.indexOf(substring, string.length - substring.length) !== -1;
    };

    APIs.query().$promise.then(function (data) {
      data.forEach(function (value) {
        var service = value['service'];
        var api = null;

        if (ends_with(service, '-extensions')) {
          // is an extension
          api = value.toJSON();
          api.title = 'Extensions';
          extensions.push(api);
        } else if (ends_with(service ,'-admin')) {
          // is an extension
          api = value.toJSON();
          api.title = 'Admin';
          extensions.push(api);
        } else {
          // is a normal service
          api = value.toJSON();
          api.section = [];
          if (!nav_by_service[service]) {
            nav_by_service[service] = {
              apis: [],
              title: value['title']};
          }
          nav_by_service[service]['apis'].push(api);
        }});

      var nest_apis = function (name_suffix) {
        for (var i = 0; i < extensions.length; i++) {
          var extension = extensions[i];
          var service = extension['service'];
          if (ends_with(service, name_suffix)) {
            var service_name = service.substr(0, service.length - name_suffix.length);
            for (var j = 0; j < nav_by_service[service_name]['apis'].length; j++) {
              if (nav_by_service[service_name]['apis'][j]['version'] === extension.version) {
                nav_by_service[service_name]['apis'][j]['section'].push(extension);
              }}}}};
      nest_apis('-extensions');
      nest_apis('-admin');
    });
    return nav_by_service;
  }])

  .controller('MenuCtrl', ['$scope', '$location', '$routeParams', '$timeout', 'navigation', 'snapRemote', function($scope, $location, $routeParams, $timeout, navigation, snapRemote) {
    $scope.filterByModel = 'by-tag';

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
    $scope.services = navigation;

  }]);
