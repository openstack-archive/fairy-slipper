// validate_test.js
// Validation of generated Swagger files
// run 'mocha' in mocha dir

'use strict';
var v = require('json-schema-remote');
var fs = require('fs');

var converted_files = ["blockstorage-v1-swagger.json",
                       "blockstorage-v2-swagger.json",
                       "compute-v2.1-swagger.json",
                       "data-processing-v1.1-swagger.json",
                       "database-v1-swagger.json",
                       "identity-admin-v2-swagger.json",
                       "identity-extensions-v2-swagger.json",
                       "identity-v2-swagger.json",
                       "identity-v3-swagger.json",
                       "image-v1-swagger.json",
                       "image-v2-swagger.json",
                       "networking-extensions-v2-swagger.json",
                       "networking-v2-swagger.json",
                       "objectstorage-v1-swagger.json"
                      ];

var i = 0;

function validate_file(filename, done) {
    var swagger_file = fs.readFileSync('../../../conversion_files_valid/'.concat(filename), 'utf8');
    var myswagger = JSON.parse(swagger_file);

    v.validate(myswagger, 'http://swagger.io/v2/schema.json', function(err, isValid) {
        if (err) {
            done(err);
            console.error('Error occurred', err);
        }
        if (isValid) {
            console.log(filename.concat(" is valid."));
            done();
        }
    });
}

// mocha test suite and tests
describe('Validate generated swagger:', function() {
    // identity and compute take some time to validate
    this.timeout(12000);
    var filen = '';

    before(function() {
        // TODO, check whether preload call is actually pre-loading the schema
        v.preload({
            $schema:'http://swagger.io/v2/schema.json',
            id:'',
            type:''
        });
    });

    beforeEach(function() {
        filen = converted_files[i];
        console.log(filen);
    });

    afterEach(function() {
        i += 1;
    });

    var j = 0;
    for (j = i; j < converted_files.length; j++) {
        // Validate each file
        it(filen, function(done) {
            validate_file(filen, done);
        });
    }
});
