# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DiskPoolTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """SKU of the VM host part of the Disk Pool deployment
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class IscsiTargetAclMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """ACL mode for iSCSI Target.
    """

    DYNAMIC = "Dynamic"
    STATIC = "Static"

class OperationalStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operational status of the resource.
    """

    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    UPDATING = "Updating"
    RUNNING = "Running"
    STOPPED = "Stopped"
    STOPPED_DEALLOCATED_ = "Stopped (deallocated)"

class ProvisioningStates(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the iSCSI Target.
    """

    INVALID = "Invalid"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PENDING = "Pending"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
