describe('Unit testing Swagger Schema rendering', function() {
  var $httpBackend,
      $compile,
      $rootScope;

  beforeEach(module('fairySlipper.browser'));
  beforeEach(module('browser/swagger-schema.html'));

  beforeEach(inject(function(_$compile_, _$rootScope_, _$httpBackend_){
    $compile = _$compile_;
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;
  }));

  afterEach(function() {
    $httpBackend.verifyNoOutstandingExpectation();
    $httpBackend.verifyNoOutstandingRequest();
  });

  it('Validate that all schema elements are rendered', function() {
    $rootScope.swagger = {"info": {"service": "identity"}};
    $rootScope.schema = [{"schema": {"$ref":"v2/authenticate-v2.0.json"},
                          "required": true,
                          "name": "body",
                          "in": "body"}];
    $httpBackend.when('GET', '/doc/identity/v2/authenticate-v2.0.json/')
      .respond({
        "type": "object",
        "properties": {
          "username": {
            "required": false,
            "type": "string1",
            "description": "Consectetuer adipiscing elit.",
            "format": ""
          },
          "password": {
            "required": false,
            "type": "string2",
            "description": "Lorem ipsum dolor sit amet.",
            "format": ""
          }}});

    var element = $compile("<swagger-schema swagger=\"swagger\" parameters=\"schema\"></swagger-schema>")($rootScope);
    $httpBackend.flush();
    $rootScope.$digest();

    expect(element.html()).toContain("username");
    expect(element.html()).toContain("Consectetuer adipiscing elit.");
    expect(element.html()).toContain("string1");

    expect(element.html()).toContain("password");
    expect(element.html()).toContain("Lorem ipsum dolor sit amet.");
    expect(element.html()).toContain("string2");
  });

  it("Empty objects don't cause failure", function() {
    $rootScope.swagger = {"info": {"service": "identity"}};
    $rootScope.schema = [{"schema": {"$ref":"v2/authenticate-v2.0.json"},
                          "required": true,
                          "name": "body",
                          "in": "body"}];
    $httpBackend.when('GET', '/doc/identity/v2/authenticate-v2.0.json/')
      .respond({});

    var element = $compile("<swagger-schema swagger=\"swagger\" parameters=\"schema\"></swagger-schema>")($rootScope);
    $httpBackend.flush();
    $rootScope.$digest();

    expect(element.html()).toBe("<ul dx-start-with=\"schema as prior\" class=\"ng-scope\"><span class=\"ng-binding ng-scope\">\n  \n  </span><!-- ngRepeat: (name, node) in prior.properties --></ul>");
  });

});
