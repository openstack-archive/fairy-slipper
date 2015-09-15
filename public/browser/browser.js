'use strict';

angular.module('fairySlipper.browser', [
  'ngRoute',
  'ngResource',
  'ngAnimate',
  'hc.marked',
  'ui.bootstrap',
  'hljs',
  'swaggerUi',
  'dotjem.angular.tree'
])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/by-path/:service/:version/', {
      templateUrl: 'browser/by-path.html',
      controller: 'ByPathCtrl'
    });
  }])

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/by-tag/:service/:version/', {
      templateUrl: 'browser/by-tag.html',
      controller: 'ByTagCtrl'
    });
  }])

  .factory('Service', ['$resource', function($resource) {
    return $resource('/doc/:service/:version/', {
    }, {
    }, {
      stripTrailingSlashes: false
    });
  }])

  .directive('swaggerExample', ['$http', function($http) {
    function link(scope, element, attrs) {
      scope.language = 'json';

      var mimes = [];
      angular.forEach(scope.source, function(value, key) {
        this.push(key);
      }, mimes);

      if (!scope.mimetype) {
        scope.mimetype = mimes[0];
      }

      var load = function(newValue, oldValue) {
        if (newValue && scope.source  && ! scope.example) {
          $http.get('/doc/' + scope.swagger.info.service + '/' +
                    scope.source[scope.mimetype].$ref +
                    '/').success(function(data){
                      // force conversion to a string.  AngularJS is too
                      // smart sometimes.
                      if (typeof data != 'string') {
                        scope.example = JSON.stringify(data, undefined, 2);
                      } else {
                        scope.example = data;
                      }
                    });
        }};

      scope.$watch('triggerLoad', load);
      if (scope.triggerLoad) {
        load();
      }
    }

    return {
      restrict: 'E',
      scope: {
        source: '=src',
        swagger: '=swagger',
        mimetype: '=mimetype',
        triggerLoad: '=triggerLoad'
      },
      link: link,
      templateUrl: 'browser/swagger-example.html'
    };
  }])

  .directive('swaggerMethod', ['$http', function($http) {
    function link(scope, element, attrs) {
      var classes = {
        get: 'label-success',
        options: 'label-success',
        head: 'label-success',
        post: 'label-primary',
        put: 'label-warning',
        patch: 'label-warning',
        copy: 'label-warning',
        delete: 'label-danger'
      };

      if (classes[scope.method]) {
        scope.label_class = classes[scope.method];
      } else {
        scope.label_class = 'label-default';
      }
    }

    return {
      restrict: 'E',
      scope: {
        method: '=method'
      },
      link: link,
      templateUrl: 'browser/swagger-method.html'
    };
  }])

  .directive('swaggerPath', ['$http', '$sce', function($http, $sce) {
    function link(scope, element, attrs) {
      var path = urldescription.parse(scope.path);
      scope.annotated_path = $sce.trustAsHtml(path.annotate(scope.parameters));
    }

    return {
      restrict: 'E',
      scope: {
        path: '=path',
        parameters: '=parameters'
      },
      link: link,
      template: '<div ng-bind-html="annotated_path"></div>'
    };
  }])

  .directive('swaggerSchema', ['$http', function($http) {
    function link(scope, element, attrs) {
      if (scope.parameters && scope.parameters[0].schema.$ref) {
        $http.get('/doc/' + scope.swagger.info.service + '/' +
                  scope.parameters[0].schema.$ref + '/')
          .success(function(data){
            scope.schema = data;
          });
      }
    }
    return {
      restrict: 'E',
      scope: {
        swagger: '=swagger',
        parameters: '=parameters'
      },
      link: link,
      templateUrl: 'browser/swagger-schema.html'
    };
  }])

  .controller('ParametersCtrl', ['$scope', function($scope) {
    $scope.parameters = {};
    angular.forEach($scope.operation.parameters, function (item) {
      if (! $scope.parameters[item.in]) {
        $scope.parameters[item.in] = [];
      }
      $scope.parameters[item.in].push(item);
    });
  }])

  .controller('ByPathCtrl', ['$scope', '$http', '$routeParams', 'Service', function($scope, $http, $routeParams, Service) {
    $scope.isEmpty = isEmpty;
    Service.get({
      service: $routeParams.service,
      version: $routeParams.version
    }).$promise.then(function (data) {
      $scope.swagger = data;
      $scope.paths = Object.keys(data.paths).map(function (key) {
        var value = data.paths[key];
        return Object.defineProperty(value, '$key', { enumerable: false, value: key});
      });
    });
  }])

  .controller('ByTagCtrl', ['$scope', '$http', '$routeParams', 'Service', function($scope, $http, $routeParams, Service) {
    $scope.isEmpty = isEmpty;
    Service.get({
      service: $routeParams.service,
      version: $routeParams.version
    }).$promise.then(function (data) {
      $scope.swagger = data;
      $scope.operations = {};
      Object.keys(data.paths).map(function (path) {
        var operations = data.paths[path];
        angular.forEach(operations, function (operation) {
          angular.forEach(operation.tags, function (tag) {
            operation['path'] = path;
            if (! $scope.operations[tag]) {
              $scope.operations[tag] = [];
            }
            $scope.operations[tag].push(operation);
          });
        });
      });
    });
  }]);
