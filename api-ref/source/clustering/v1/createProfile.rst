
Create profile
==============

.. rest_method::  POST /v1/profiles

Creates a profile.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - spec: spec
   - name: name
   - metadata: metadata

Request Example
---------------

.. literalinclude:: ../samples/profile-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - location: location
   - profile: profile





