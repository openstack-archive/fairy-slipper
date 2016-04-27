
List policies
=============

.. rest_method::  GET /v1/policies

Lists all policies.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort: sort
   - global_project: global_project
   - name: name
   - type: type



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - policies: policies




Response Example
----------------

.. literalinclude:: ../samples/policies-list-response.json
   :language: javascript



