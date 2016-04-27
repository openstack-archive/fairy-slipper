
Create metering label rule
==========================

.. rest_method::  POST /v2.0/metering/metering-label-rules

Creates an L3 metering label rule.

Error response codes:201,404,403,401,400,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - remote_ip_prefix: remote_ip_prefix
   - direction: direction
   - metering_label_id: metering_label_id
   - metering_label_rule: metering_label_rule
   - excluded: excluded

Request Example
---------------

.. literalinclude:: ../samples/metering-labels/metering-label-rule-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - direction: direction
   - remote_ip_prefix: remote_ip_prefix
   - excluded : excluded 
   - metering_label_id: metering_label_id
   - metering_label_rule: metering_label_rule
   - id: id










