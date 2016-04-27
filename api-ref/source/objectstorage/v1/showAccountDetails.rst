
Show account details and list containers
========================================

.. rest_method::  GET /v1/{account}

Shows details for an account and lists containers, sorted by name, in the account.

The sort order for the name is based on a binary comparison, a
single built-in collating sequence that compares string data by
using the SQLite memcmp() function, regardless of text encoding.
See `Collating Sequences
<http://www.sqlite.org/datatype3.html#collation>`_.

Example requests and responses:

- Show account details and list containers and ask for a JSON
  response:

  ::

     curl -i $publicURL?format=json -X GET -H "X-Auth-Token: $token"


- List containers and ask for an XML response:

  ::

     curl -i $publicURL?format=xml -X GET -H "X-Auth-Token: $token"


The response body returns a list of containers. The default
response (``text/plain``) returns one container per line.

If you use query parameters to page through a long list of
containers, you have reached the end of the list if the number of
items in the returned list is less than the request ``limit``
value. The list contains more items if the number of items in the
returned list equals the ``limit`` value.

When asking for a list of containers and there are none, the
response behavior changes depending on whether the request format
is text, JSON, or XML. For a text response, you get a 204 , because
there is no content. However, for a JSON or XML response, you get a
200 with content indicating an empty array.

If the request succeeds, the operation returns one of these status
codes:

- ``OK (200)``. Success. The response body lists the containers.

- ``No Content (204)``. Success. The response body shows no
  containers. Either the account has no containers or you are
  paging through a long list of names by using the ``marker``,
  ``limit``, or ``end_marker`` query parameter and you have reached
  the end of the list.


Normal response codes: 200
Error response codes:204,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - account: account
   - limit: limit
   - marker: marker
   - end_marker: end_marker
   - format: format
   - prefix: prefix
   - delimiter: delimiter
   - X-Auth-Token: X-Auth-Token
   - X-Newest: X-Newest
   - Accept: Accept
   - X-Trans-Id-Extra: X-Trans-Id-Extra



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length
   - X-Account-Meta-name: X-Account-Meta-name
   - X-Account-Object-Count: X-Account-Object-Count
   - X-Account-Meta-Temp-URL-Key-2: X-Account-Meta-Temp-URL-Key-2
   - X-Timestamp: X-Timestamp
   - X-Account-Meta-Temp-URL-Key: X-Account-Meta-Temp-URL-Key
   - X-Trans-Id: X-Trans-Id
   - Date: Date
   - X-Account-Bytes-Used: X-Account-Bytes-Used
   - X-Account-Container-Count: X-Account-Container-Count
   - Content-Type: Content-Type
   - count: count
   - bytes: bytes
   - name: name




Response Example
----------------

.. literalinclude:: samples/account-containers-list-http-response-xml.txt
   :language: javascript




