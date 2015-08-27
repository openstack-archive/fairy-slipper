
describe("A suite", function() {
  it("contains spec with an expectation", function() {
    var emailUrl = urldescription.parse('{tenant_id}/servers/{server_id}');

    expect(emailUrl.annotate({
      email: 'user@domain',
      folder: 'test',
      id: 42
    })).toBe('{tenant_id}/servers/{server_id}');
  });
});

describe("A suite", function() {
  it("contains spec with an expectation", function() {
    var emailUrl = urldescription.parse('{tenant_id}/servers/{server_id}');

    expect(emailUrl.annotate({
      tenant_id: 'test_tenant',
      server_id: 'test_server'
    })).toBe('test_tenant/servers/test_server');
  });
});
