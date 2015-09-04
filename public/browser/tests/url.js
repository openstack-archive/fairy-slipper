
describe("A suite", function() {
  it("contains spec with an expectation", function() {
    var emailUrl = urldescription.parse('{tenant_id}/servers/{server_id}');

    expect(emailUrl.annotate([{"required":true,
                               "in":"path",
                               "type":"string",
                               "name":"alias",
                               "description":"The extension name."
                              }]))
      .toBe('{tenant_id}/servers/{server_id}');
  });
});

describe("A suite", function() {
  it("contains spec with an expectation", function() {
    var emailUrl = urldescription.parse('{tenant_id}/servers/{server_id}');

    expect(emailUrl.annotate([{"required":true,
                               "in":"path",
                               "type":"string",
                               "name":"tenant_id",
                               "description":"The id of the tenant."
                              },
                              {"required":true,
                               "in":"path",
                               "type":"string",
                               "name":"server_id",
                               "description":"The id of the server."
                              }]))
      .toBe('<abbr title="The id of the tenant.">{tenant_id}</abbr>/servers/<abbr title="The id of the server.">{server_id}</abbr>');
  });
});
