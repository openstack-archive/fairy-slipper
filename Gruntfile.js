
module.exports = function(grunt) {
  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  var proxySnippet =
        require('grunt-connect-proxy/lib/utils').proxyRequest;

  grunt.initConfig({
	pkg: grunt.file.readJSON('package.json'),
    // The actual grunt server settings
    // Watches files for changes and runs tasks based on the changed files
    watch: {
      all: {
        options: {
          nospawn: true
        },
        files: [
          'public/**/*.html',
          'public/**/*.css',
          'public/**/*.js',
          'public/**/*.{png,jpg,jpeg,gif,webp,svg}'
        ],
        tasks: ["default"]
      }
    },
    reload: {
      port: 9000,
      liveReload: {},
      proxy: {
        host: "localhost",
        port: 8080
      }
    }
  });

  grunt.registerTask('default', [
    'reload',
    'watch'
  ]);

};
