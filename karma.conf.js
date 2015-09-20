module.exports = function(config){
  var configuration = {

    basePath : './public/',

    files : [
      "components/angular/angular.js",
      "components/angular-mocks/angular-mocks.js",
      "components/angular-route/angular-route.js",
      "components/angular-resource/angular-resource.js",
      "components/angular-animate/angular-animate.js",
      "components/angular-bootstrap/ui-bootstrap-tpls.js",
      "components/angular-snap/angular-snap.js",
      "components/snapjs/snap.js",
      "components/angular-marked/angular-marked.js",
      "components/marked/marked.min.js",
      "components/highlightjs/highlight.pack.js",
      "components/angular-highlightjs/angular-highlightjs.js",
      "components/dotjem-angular-tree/dotjem-angular-tree.js",
      'app.js',
      'browser/*.js',
      'browser/**/*.js',
      'browser/*.html'
    ],

    autoWatch : true,

    preprocessors: {
        'browser/*.html': ['ng-html2js']
    },

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
      'karma-chrome-launcher',
      'karma-firefox-launcher',
      'karma-jasmine',
      'karma-ng-html2js-preprocessor',
      'karma-junit-reporter'
    ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    },

    customLaunchers: {
      Chrome_travis_ci: {
        base: 'Chrome',
        flags: ['--no-sandbox']
      }
    }
  };

  if(process.env.TRAVIS){
    configuration.browsers = ['Chrome_travis_ci'];
  }

  config.set(configuration);
};
