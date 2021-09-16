// Karma is a console tool for running tests. it can track source code changes and display the percentage of code tests coverage. It is adjusted using the configuration file karma.conf.js(HERE), where the paths to tested files and to the files with tests should be specified.

// config/karma.config.js

module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;

  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';

  var coverageFiles = [
    __dirname + '/../opal_practice/static/js/opal_practice/**/*.js',
    // Add code to include on test runs here ...
  ];

  var includedFiles = [
    'opal/app.js',

    // Add test cases here
    __dirname + '/../opal_practice/static/js/tests/**/*.js',
  ].concat(coverageFiles);

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};