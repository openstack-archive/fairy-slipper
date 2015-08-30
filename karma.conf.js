module.exports = function(config){
  var configuration = {

    basePath : './',

    files : [
      "public/components/angular/angular.js",
      "public/components/angular-route/angular-route.js",
      "public/components/angular-resource/angular-resource.js",
      "public/components/angular-animate/angular-animate.js",
      "public/components/angular-swagger-ui/dist/scripts/swagger-ui.js",
      "public/components/angular-bootstrap/ui-bootstrap-tpls.js",
      "public/components/angular-snap/angular-snap.js",
      "public/components/snapjs/snap.js",
      "public/components/angular-marked/angular-marked.js",
      "public/components/marked/marked.min.js",
      "public/components/highlightjs/highlight.pack.js",
      "public/components/angular-highlightjs/angular-highlightjs.js",
      'public/browser/*.js',
      'public/browser/**/*.js',
      'public/app.js'
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-firefox-launcher',
            'karma-jasmine',
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
