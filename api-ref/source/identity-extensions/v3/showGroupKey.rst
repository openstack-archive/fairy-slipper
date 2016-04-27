
Show group key
==============

.. rest_method::  GET /v3/groups

Shows the key for a group in the KDS.

When a ticket is requested where the destination is a group, a
group key is generated that is valid for a predetermined amount of
time. Any member of the group can get the key as long as it is
still valid. Group keys are necessary to verify signatures and
decrypt messages that have a group name as the target.

Error response codes:201,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name












