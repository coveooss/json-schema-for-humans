# Schema Docs

- [1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `root > storage`](#storage)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage_anyOf_i0)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage_anyOf_i1)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage_anyOf_i2)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage_anyOf_i3)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|+  [storage](#storage)|No|object|No|-|

## <a name="storage"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `root > storage`

| Type | `combining` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

| Any of(Option) | 
| ---- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1) |
| [item 2](#storage_anyOf_i2) |
| [tmpfs](#storage_anyOf_i3) |
### <a name="storage_anyOf_i0"></a>1.1. Property `root > storage > anyOf > diskDevice`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/diskDevice |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

### <a name="storage_anyOf_i1"></a>1.2. Property `root > storage > anyOf > diskUUID`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/diskUUID |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

### <a name="storage_anyOf_i2"></a>1.3. Property `root > storage > anyOf > item 2`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

### <a name="storage_anyOf_i3"></a>1.4. Property `root > storage > anyOf > tmpfs`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/tmpfs |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 22:25:45 +0100