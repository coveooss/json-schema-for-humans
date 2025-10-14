# Schema Docs

- [1. ![Required](https://img.shields.io/badge/Required-blue) Property`root > storage`](#storage)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage_anyOf_i0)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage_anyOf_i1)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage_anyOf_i2)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage_anyOf_i3)

|          |          |
| -------- | -------- |
| **Type** | `object` |

**Description:** JSON Schema for an fstab entry

| Property               | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [storage](#storage ) | No      | Combination | No         | -          | -                 |

## <a name="storage"></a>1. ![Required](https://img.shields.io/badge/Required-blue) Property`root > storage`

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

| Any of(Option)                  |
| ------------------------------- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1)   |
| [item 2](#storage_anyOf_i2)     |
| [tmpfs](#storage_anyOf_i3)      |

### <a name="storage_anyOf_i0"></a>1.1. Property `root > storage > anyOf > diskDevice`

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `object`                 |
| **Defined in** | #/definitions/diskDevice |

### <a name="storage_anyOf_i1"></a>1.2. Property `root > storage > anyOf > diskUUID`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `object`               |
| **Defined in** | #/definitions/diskUUID |

### <a name="storage_anyOf_i2"></a>1.3. Property `root > storage > anyOf > item 2`

|          |          |
| -------- | -------- |
| **Type** | `object` |

### <a name="storage_anyOf_i3"></a>1.4. Property `root > storage > anyOf > tmpfs`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `object`            |
| **Defined in** | #/definitions/tmpfs |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
