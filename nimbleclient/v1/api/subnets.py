#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

from ..resource import Resource, Collection
from ..exceptions import NimOSAPIOperationUnsupported

class Subnet(Resource):
    """
    Search subnets information. Many networking tasks require that objects such as replication partners are either on the same network or have a route to a secondary network. Subnets let you create logical addressing for selective routing.

    Parameters:
    - id                   : Identifier for the initiator group.
    - name                 : Name of subnet configuration.
    - network              : Subnet network address.
    - netmask              : Subnet netmask address.
    - type                 : Subnet type. Options include 'mgmt', 'data', and 'mgmt,data'.
    - allow_iscsi          : Subnet type.
    - allow_group          : Subnet type.
    - discovery_ip         : Subnet network address.
    - mtu                  : MTU for specified subnet. Valid MTU's are in the 512-16000 range.
    - netzone_type         : Specify Network Affinity Zone type for iSCSI enabled subnets. Valid types are Single, Bisect, and EvenOdd for iSCSI subnets.
    - vlan_id              : VLAN ID for specified subnet. Valid ID's are in the 1-4094 range.
    - creation_time        : Time when this subnet configuration was created.
    - last_modified        : Time when this subnet configuration was last modified.
    - failover             : Failover setting of the subnet.
    - failover_enable_time : Failover for this subnet will be enabled again at the time specified by failover_enable_time.
    """

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")

class SubnetList(Collection):
    resource = Subnet
    resource_type = "subnets"

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
