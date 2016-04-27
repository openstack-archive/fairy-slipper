
List tasks
==========

.. rest_method::  GET /v2/tasks

Lists tasks.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - sort_dir: sort_dir
   - sort_key: sort_key
   - type: type
   - status: status



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tasks: tasks
   - type: type
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/tasks-list-response.json
   :language: javascript



