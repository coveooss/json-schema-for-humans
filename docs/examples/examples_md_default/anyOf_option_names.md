# Schema Docs

- [1. Property `root > storage`](#storage-72616765)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage_anyOf_i0-665f6930)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage_anyOf_i1-665f6931)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage_anyOf_i2-665f6932)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage_anyOf_i3-665f6933)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** JSON Schema for an fstab entry

| Property                        | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [storage](#storage-72616765 ) | No      | Combination | No         | -          | -                 |

## <a name="storage-72616765"></a>1. Property `root > storage`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Any of(Option)                           |
| ---------------------------------------- |
| [diskDevice](#storage_anyOf_i0-665f6930) |
| [diskUUID](#storage_anyOf_i1-665f6931)   |
| [item 2](#storage_anyOf_i2-665f6932)     |
| [tmpfs](#storage_anyOf_i3-665f6933)      |

### <a name="storage_anyOf_i0-665f6930"></a>1.1. Property `root > storage > anyOf > diskDevice`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskDevice                                                  |

### <a name="storage_anyOf_i1-665f6931"></a>1.2. Property `root > storage > anyOf > diskUUID`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskUUID                                                    |

### <a name="storage_anyOf_i2-665f6932"></a>1.3. Property `root > storage > anyOf > item 2`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

### <a name="storage_anyOf_i3-665f6933"></a>1.4. Property `root > storage > anyOf > tmpfs`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/tmpfs                                                       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
