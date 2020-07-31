# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ReasonCode(str, Enum):

    quota_id = "QuotaId"
    not_available_for_subscription = "NotAvailableForSubscription"


class SkuName(str, Enum):

    standard_lrs = "Standard_LRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"


class SkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class Kind(str, Enum):

    storage = "Storage"
    storage_v2 = "StorageV2"
    blob_storage = "BlobStorage"


class Reason(str, Enum):

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"


class KeySource(str, Enum):

    microsoft_storage = "Microsoft.Storage"
    microsoft_keyvault = "Microsoft.Keyvault"


class Action(str, Enum):

    allow = "Allow"


class State(str, Enum):

    provisioning = "provisioning"
    deprovisioning = "deprovisioning"
    succeeded = "succeeded"
    failed = "failed"
    network_source_deleted = "networkSourceDeleted"


class Bypass(str, Enum):

    none = "None"
    logging = "Logging"
    metrics = "Metrics"
    azure_services = "AzureServices"


class DefaultAction(str, Enum):

    allow = "Allow"
    deny = "Deny"


class AccessTier(str, Enum):

    hot = "Hot"
    cool = "Cool"


class ProvisioningState(str, Enum):

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"


class AccountStatus(str, Enum):

    available = "available"
    unavailable = "unavailable"


class KeyPermission(str, Enum):

    read = "Read"
    full = "Full"


class UsageUnit(str, Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    counts_per_second = "CountsPerSecond"
    bytes_per_second = "BytesPerSecond"


class Services(str, Enum):

    b = "b"
    q = "q"
    t = "t"
    f = "f"


class SignedResourceTypes(str, Enum):

    s = "s"
    c = "c"
    o = "o"


class Permissions(str, Enum):

    r = "r"
    d = "d"
    w = "w"
    l = "l"
    a = "a"
    c = "c"
    u = "u"
    p = "p"


class HttpProtocol(str, Enum):

    httpshttp = "https,http"
    https = "https"


class SignedResource(str, Enum):

    b = "b"
    c = "c"
    f = "f"
    s = "s"