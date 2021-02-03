

# Schema Docs

Type: `object`

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="storage"></a>1.  Property `root > storage`

| Node | 
| ---- |
| [diskDevice](#storage_oneOf_i0) |
| [diskUUID](#storage_oneOf_i1) |
| [nfs](#storage_oneOf_i2) |
| [tmpfs](#storage_oneOf_i3) |
###  <a name="storage"></a>1.1.  Property `root > storage > oneOf > diskDevice`

Type: `object`

Defined in: #/definitions/diskDevice

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |
###  <a name="storage"></a>1.2.  Property `root > storage > oneOf > diskUUID`

Type: `object`

Defined in: #/definitions/diskUUID

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |
###  <a name="storage"></a>1.3.  Property `root > storage > oneOf > nfs`

Type: `object`

Defined in: #/definitions/nfs

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |
###  <a name="storage"></a>1.4.  Property `root > storage > oneOf > tmpfs`

Type: `object`

Defined in: #/definitions/tmpfs

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:49 +0100