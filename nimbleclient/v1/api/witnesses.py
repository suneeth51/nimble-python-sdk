#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class Witness(Resource):
    """
    Manage witness host configuration.

    Parameters:
    - id                       : Identifier of the witness configuration.
    - username                 : Username of witness. This has to be a non-root that can login to the witness host.
    - password                 : Password of witness.
    - host                     : Hostname or ip addresses of witness.
    - port                     : Port of witness.
    - secure_mode              : To verify the witness host against CA cert and to apply possible security modes.
    - auto_switchover_messages : List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found.
    """

    def test(self):
        """
        Tests and validates witness configuration between the array and the witness.

        Parameters:
        - id : ID of the witness.
        """

        return self.collection.test(self.id)

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")

class WitnessList(Collection):
    resource = Witness
    resource_type = "witnesses"

    def test(self, id):
        """
        Tests and validates witness configuration between the array and the witness.

        Parameters:
        - id : ID of the witness.
        """

        return self._client.perform_resource_action(self.resource_type, id, 'test', id=id)

    def create(self, **kwargs):
        resp = self._client.create_resource(self.resource_type, **kwargs)
        return self.resource(resp['id'], resp, client=self._client, collection=self)

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
