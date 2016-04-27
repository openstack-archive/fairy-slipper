
Update alarm
============

.. rest_method::  PUT /v2/alarms/{alarm_id}

Updates an alarm.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - alarm_id: alarm_id
   - data: data



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - alarm_actions: alarm_actions
   - ok_actions: ok_actions
   - description: description
   - timestamp: timestamp
   - enabled: enabled
   - combination_rule: combination_rule
   - state_timestamp: state_timestamp
   - threshold_rule: threshold_rule
   - alarm_id: alarm_id
   - state: state
   - insufficient_data_actions: insufficient_data_actions
   - repeat_actions: repeat_actions
   - user_id: user_id
   - project_id: project_id
   - type: type
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/alarm-show-response.json
   :language: javascript



