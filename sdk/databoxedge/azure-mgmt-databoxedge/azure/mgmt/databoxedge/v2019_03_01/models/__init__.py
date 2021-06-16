# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ARMBaseModel
    from ._models_py3 import Address
    from ._models_py3 import Alert
    from ._models_py3 import AlertErrorDetails
    from ._models_py3 import AlertList
    from ._models_py3 import AsymmetricEncryptedSecret
    from ._models_py3 import Authentication
    from ._models_py3 import AzureContainerInfo
    from ._models_py3 import BandwidthSchedule
    from ._models_py3 import BandwidthSchedulesList
    from ._models_py3 import ClientAccessRight
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ContactDetails
    from ._models_py3 import DataBoxEdgeDevice
    from ._models_py3 import DataBoxEdgeDeviceExtendedInfo
    from ._models_py3 import DataBoxEdgeDeviceList
    from ._models_py3 import DataBoxEdgeDevicePatch
    from ._models_py3 import FileEventTrigger
    from ._models_py3 import FileSourceInfo
    from ._models_py3 import IoTDeviceInfo
    from ._models_py3 import IoTRole
    from ._models_py3 import Ipv4Config
    from ._models_py3 import Ipv6Config
    from ._models_py3 import Job
    from ._models_py3 import JobErrorDetails
    from ._models_py3 import JobErrorItem
    from ._models_py3 import MetricDimensionV1
    from ._models_py3 import MetricSpecificationV1
    from ._models_py3 import MountPointMap
    from ._models_py3 import NetworkAdapter
    from ._models_py3 import NetworkAdapterPosition
    from ._models_py3 import NetworkSettings
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationsList
    from ._models_py3 import Order
    from ._models_py3 import OrderList
    from ._models_py3 import OrderStatus
    from ._models_py3 import PeriodicTimerEventTrigger
    from ._models_py3 import PeriodicTimerSourceInfo
    from ._models_py3 import RefreshDetails
    from ._models_py3 import Role
    from ._models_py3 import RoleList
    from ._models_py3 import RoleSinkInfo
    from ._models_py3 import SecuritySettings
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Share
    from ._models_py3 import ShareAccessRight
    from ._models_py3 import ShareList
    from ._models_py3 import Sku
    from ._models_py3 import StorageAccountCredential
    from ._models_py3 import StorageAccountCredentialList
    from ._models_py3 import SymmetricKey
    from ._models_py3 import TrackingInfo
    from ._models_py3 import Trigger
    from ._models_py3 import TriggerList
    from ._models_py3 import UpdateDownloadProgress
    from ._models_py3 import UpdateInstallProgress
    from ._models_py3 import UpdateSummary
    from ._models_py3 import UploadCertificateRequest
    from ._models_py3 import UploadCertificateResponse
    from ._models_py3 import User
    from ._models_py3 import UserAccessRight
    from ._models_py3 import UserList
except (SyntaxError, ImportError):
    from ._models import ARMBaseModel  # type: ignore
    from ._models import Address  # type: ignore
    from ._models import Alert  # type: ignore
    from ._models import AlertErrorDetails  # type: ignore
    from ._models import AlertList  # type: ignore
    from ._models import AsymmetricEncryptedSecret  # type: ignore
    from ._models import Authentication  # type: ignore
    from ._models import AzureContainerInfo  # type: ignore
    from ._models import BandwidthSchedule  # type: ignore
    from ._models import BandwidthSchedulesList  # type: ignore
    from ._models import ClientAccessRight  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ContactDetails  # type: ignore
    from ._models import DataBoxEdgeDevice  # type: ignore
    from ._models import DataBoxEdgeDeviceExtendedInfo  # type: ignore
    from ._models import DataBoxEdgeDeviceList  # type: ignore
    from ._models import DataBoxEdgeDevicePatch  # type: ignore
    from ._models import FileEventTrigger  # type: ignore
    from ._models import FileSourceInfo  # type: ignore
    from ._models import IoTDeviceInfo  # type: ignore
    from ._models import IoTRole  # type: ignore
    from ._models import Ipv4Config  # type: ignore
    from ._models import Ipv6Config  # type: ignore
    from ._models import Job  # type: ignore
    from ._models import JobErrorDetails  # type: ignore
    from ._models import JobErrorItem  # type: ignore
    from ._models import MetricDimensionV1  # type: ignore
    from ._models import MetricSpecificationV1  # type: ignore
    from ._models import MountPointMap  # type: ignore
    from ._models import NetworkAdapter  # type: ignore
    from ._models import NetworkAdapterPosition  # type: ignore
    from ._models import NetworkSettings  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationsList  # type: ignore
    from ._models import Order  # type: ignore
    from ._models import OrderList  # type: ignore
    from ._models import OrderStatus  # type: ignore
    from ._models import PeriodicTimerEventTrigger  # type: ignore
    from ._models import PeriodicTimerSourceInfo  # type: ignore
    from ._models import RefreshDetails  # type: ignore
    from ._models import Role  # type: ignore
    from ._models import RoleList  # type: ignore
    from ._models import RoleSinkInfo  # type: ignore
    from ._models import SecuritySettings  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import Share  # type: ignore
    from ._models import ShareAccessRight  # type: ignore
    from ._models import ShareList  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import StorageAccountCredential  # type: ignore
    from ._models import StorageAccountCredentialList  # type: ignore
    from ._models import SymmetricKey  # type: ignore
    from ._models import TrackingInfo  # type: ignore
    from ._models import Trigger  # type: ignore
    from ._models import TriggerList  # type: ignore
    from ._models import UpdateDownloadProgress  # type: ignore
    from ._models import UpdateInstallProgress  # type: ignore
    from ._models import UpdateSummary  # type: ignore
    from ._models import UploadCertificateRequest  # type: ignore
    from ._models import UploadCertificateResponse  # type: ignore
    from ._models import User  # type: ignore
    from ._models import UserAccessRight  # type: ignore
    from ._models import UserList  # type: ignore

from ._data_box_edge_management_client_enums import (
    AccountType,
    AlertSeverity,
    AuthenticationType,
    AzureContainerDataFormat,
    ClientPermissionType,
    DataBoxEdgeDeviceStatus,
    DataPolicy,
    DayOfWeek,
    DeviceType,
    DownloadPhase,
    EncryptionAlgorithm,
    InstallRebootBehavior,
    JobStatus,
    JobType,
    MetricAggregationType,
    MetricCategory,
    MetricUnit,
    MonitoringStatus,
    NetworkAdapterDHCPStatus,
    NetworkAdapterRDMAStatus,
    NetworkAdapterStatus,
    NetworkGroup,
    OrderState,
    PlatformType,
    RoleStatus,
    RoleTypes,
    SSLStatus,
    ShareAccessProtocol,
    ShareAccessType,
    ShareStatus,
    SkuName,
    SkuTier,
    TimeGrain,
    TriggerEventType,
    UpdateOperation,
    UpdateOperationStage,
)

__all__ = [
    'ARMBaseModel',
    'Address',
    'Alert',
    'AlertErrorDetails',
    'AlertList',
    'AsymmetricEncryptedSecret',
    'Authentication',
    'AzureContainerInfo',
    'BandwidthSchedule',
    'BandwidthSchedulesList',
    'ClientAccessRight',
    'CloudErrorBody',
    'ContactDetails',
    'DataBoxEdgeDevice',
    'DataBoxEdgeDeviceExtendedInfo',
    'DataBoxEdgeDeviceList',
    'DataBoxEdgeDevicePatch',
    'FileEventTrigger',
    'FileSourceInfo',
    'IoTDeviceInfo',
    'IoTRole',
    'Ipv4Config',
    'Ipv6Config',
    'Job',
    'JobErrorDetails',
    'JobErrorItem',
    'MetricDimensionV1',
    'MetricSpecificationV1',
    'MountPointMap',
    'NetworkAdapter',
    'NetworkAdapterPosition',
    'NetworkSettings',
    'Operation',
    'OperationDisplay',
    'OperationsList',
    'Order',
    'OrderList',
    'OrderStatus',
    'PeriodicTimerEventTrigger',
    'PeriodicTimerSourceInfo',
    'RefreshDetails',
    'Role',
    'RoleList',
    'RoleSinkInfo',
    'SecuritySettings',
    'ServiceSpecification',
    'Share',
    'ShareAccessRight',
    'ShareList',
    'Sku',
    'StorageAccountCredential',
    'StorageAccountCredentialList',
    'SymmetricKey',
    'TrackingInfo',
    'Trigger',
    'TriggerList',
    'UpdateDownloadProgress',
    'UpdateInstallProgress',
    'UpdateSummary',
    'UploadCertificateRequest',
    'UploadCertificateResponse',
    'User',
    'UserAccessRight',
    'UserList',
    'AccountType',
    'AlertSeverity',
    'AuthenticationType',
    'AzureContainerDataFormat',
    'ClientPermissionType',
    'DataBoxEdgeDeviceStatus',
    'DataPolicy',
    'DayOfWeek',
    'DeviceType',
    'DownloadPhase',
    'EncryptionAlgorithm',
    'InstallRebootBehavior',
    'JobStatus',
    'JobType',
    'MetricAggregationType',
    'MetricCategory',
    'MetricUnit',
    'MonitoringStatus',
    'NetworkAdapterDHCPStatus',
    'NetworkAdapterRDMAStatus',
    'NetworkAdapterStatus',
    'NetworkGroup',
    'OrderState',
    'PlatformType',
    'RoleStatus',
    'RoleTypes',
    'SSLStatus',
    'ShareAccessProtocol',
    'ShareAccessType',
    'ShareStatus',
    'SkuName',
    'SkuTier',
    'TimeGrain',
    'TriggerEventType',
    'UpdateOperation',
    'UpdateOperationStage',
]
