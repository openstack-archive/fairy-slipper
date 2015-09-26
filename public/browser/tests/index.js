describe('Unit testing navigation creation', function() {
  var mock, navigation;
  beforeEach(module('fairySlipper.index'));
  beforeEach(module('browser/index.html'));


  beforeEach(inject(function(_$compile_, _$rootScope_, _$httpBackend_){
    $compile = _$compile_;
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;

    inject(function($injector) {
      navigation = $injector.get('navigation');
    });
  }));

  afterEach(function() {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });


  it('It should return the navigation', function() {
    $httpBackend.when('GET', '/doc')
      .respond([
        {
          "version": "v2",
          "service": "identity",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Identity"
        },
        {
          "version": "v1",
          "service": "database",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Database Service"
        },
        {
          "version": "v3",
          "service": "identity",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Identity"
        }]);
    $httpBackend.flush();
    $rootScope.$digest();

    expect(Object.keys(navigation).sort()).toEqual(['database', 'identity'].sort());

    expect(navigation).toEqual(
      {
        identity: {
          apis: [{version: 'v2',
                  service: 'identity',
                  license: {url: 'http://www.apache.org/licenses/LICENSE-2.0.html', name: 'Apache 2.0'},
                  section: [],
                  title: 'Identity'},
                 {version: 'v3',
                  service: 'identity',
                  license: {url: 'http://www.apache.org/licenses/LICENSE-2.0.html', name: 'Apache 2.0' },
                  section: [],
                  title: 'Identity' }],
          title: 'Identity' },
        database: {
          apis: [{version: 'v1',
                  service: 'database',
                  license: {url: 'http://www.apache.org/licenses/LICENSE-2.0.html', name: 'Apache 2.0'},
                  section: [],
                  title: 'Database Service' }],
          title: 'Database Service'}}
    );
  });

  it('It should return the navigation', function() {
    $httpBackend.when('GET', '/doc')
      .respond([
        {
          "version": "v2",
          "service": "identity",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Identity"
        },
        {
          "version": "v1",
          "service": "database",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Database Service"
        },
        {
          "version": "v2",
          "service": "identity-extensions",
          "license": {
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
            "name": "Apache 2.0"
          },
          "title": "Identity"
        }]);
    $httpBackend.flush();
    $rootScope.$digest();

    expect(Object.keys(navigation).sort()).toEqual(['database', 'identity'].sort());

    expect(navigation).toEqual(
      {
        identity: {
          apis: [{version: 'v2',
                  service: 'identity',
                  license: {url: 'http://www.apache.org/licenses/LICENSE-2.0.html', name: 'Apache 2.0'},
                  section: [{
                    "version": "v2",
                    "service": "identity-extensions",
                    "license": {
                      "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
                      "name": "Apache 2.0"
                    },
                    "title": "Extensions"
                  }],
                  title: 'Identity'}],
          title: 'Identity' },
        database: {
          apis: [{version: 'v1',
                  service: 'database',
                  license: {url: 'http://www.apache.org/licenses/LICENSE-2.0.html', name: 'Apache 2.0'},
                  section: [],
                  title: 'Database Service' }],
          title: 'Database Service'}}
    );
  });
});
