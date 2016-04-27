
Show task details
=================

.. rest_method::  GET /v2/tasks/{task_id}

Shows details for a task.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - task_id: task_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - type: type
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/task-show-response.json
   :language: javascript



