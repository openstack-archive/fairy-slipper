
List flavors
============

.. rest_method::  GET /v2.0/flavors

Lists all flavors visible for the tenant account.

The list can be empty.

Standard query parameters are supported on the URI. For example,
``fields`` can be used to limit the returned response to just name
by appending ``?fields=name``. If Neutron configuration supports
pagination by overriding allow_pagination = false, the ``marker``
query parameter can set the last element id the client has seen and
``limit`` set the maximum number of items to return. if Neutron
configuration has allow_sorting = true, ``sort_key`` and
``sort_dir`` pairs can be used where sort direction is 'asc' or
'desc'.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - flavors: flavors
   - description: description
   - enabled: enabled
   - service_profiles: service_profiles
   - service_type: service_type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/flavors/flavors-list-response.json
   :language: javascript




