
Show metering label rule details
================================

.. rest_method::  GET /v2.0/metering/metering-label-rules/{metering-label-rule-id}

Shows details for a metering label rule.

The response body shows this information for each metering label
rule:

- ``direction``. Either ingress or egress.

- ``excluded``. Either ``true`` or ``false``.

- The UUID for the metering label rule.

- The remote IP prefix.

- The metering label ID for the metering label with which the rule
  is associated.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: ../samples/metering-labels/metering-label-rule-show-response.json
   :language: javascript





