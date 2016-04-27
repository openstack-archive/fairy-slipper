
List profiles
=============

.. rest_method::  GET /v1/profiles

Lists all profiles.


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
   - metadata: metadata



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - profiles: profiles




Response Example
----------------

.. literalinclude:: ../samples/profiles-list-response.json
   :language: javascript



