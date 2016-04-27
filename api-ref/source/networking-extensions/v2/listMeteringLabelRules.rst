
List metering label rules
=========================

.. rest_method::  GET /v2.0/metering/metering-label-rules

Lists a summary of all L3 metering label rules that belong to the tenant.

The list shows the UUID for each metering label rule.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - direction: direction
   - remote_ip_prefix: remote_ip_prefix
   - metering_label_rules: metering_label_rules
   - excluded : excluded 
   - metering_label_id: metering_label_id
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/metering-labels/metering-label-rules-list-response.json
   :language: javascript




