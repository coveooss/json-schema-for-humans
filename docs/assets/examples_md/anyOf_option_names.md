# Schema Docs

- [1. Property `root > storage`](#storage)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage)

Type: `object`

**Description:** JSON Schema for an fstab entry
| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="storage"></a>1. Property `root > storage`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Any of(Option) | 
| ---- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1) |
| [Any of(Option) 3](#storage_anyOf_i2) |
| [tmpfs](#storage_anyOf_i3) |
### <a name="storage"></a>1.1. Property `root > storage > anyOf > diskDevice`
Type: `object`

Defined in: #/definitions/diskDevice

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="storage"></a>1.2. Property `root > storage > anyOf > diskUUID`
Type: `object`

Defined in: #/definitions/diskUUID

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="storage"></a>1.3. Property `root > storage > anyOf > item 2`
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="storage"></a>1.4. Property `root > storage > anyOf > tmpfs`
Type: `object`

Defined in: #/definitions/tmpfs

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 12:13:15 +0100