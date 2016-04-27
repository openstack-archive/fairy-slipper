
List groups to which a user belongs
===================================

.. rest_method::  GET /v3/users/{user_id}/groups

Lists groups to which a user belongs.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id






Response Example
----------------

.. literalinclude:: ../samples/admin/user-groups-list-response.json
   :language: javascript










