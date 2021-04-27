# Schema Docs

- [1. [Required] Property `root > storage`](#storage)
  - [1.1. Property `root > storage > oneOf > diskDevice`](#storage_oneOf_i0)
  - [1.2. Property `root > storage > oneOf > diskUUID`](#storage_oneOf_i1)
  - [1.3. Property `root > storage > oneOf > nfs`](#storage_oneOf_i2)
  - [1.4. Property `root > storage > oneOf > tmpfs`](#storage_oneOf_i3)

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** JSON Schema for an fstab entry

| Property               | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [storage](#storage ) | No      | Combination | No         | -          | -                 |
|                        |         |             |            |            |                   |

## <a name="storage"></a>1. [Required] Property `root > storage`

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| One of(Option)                  |
| ------------------------------- |
| [diskDevice](#storage_oneOf_i0) |
| [diskUUID](#storage_oneOf_i1)   |
| [nfs](#storage_oneOf_i2)        |
| [tmpfs](#storage_oneOf_i3)      |
|                                 |

### <a name="storage_oneOf_i0"></a>1.1. Property `root > storage > oneOf > diskDevice`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskDevice                                                  |
|                           |                                                                           |

### <a name="storage_oneOf_i1"></a>1.2. Property `root > storage > oneOf > diskUUID`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskUUID                                                    |
|                           |                                                                           |

### <a name="storage_oneOf_i2"></a>1.3. Property `root > storage > oneOf > nfs`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/nfs                                                         |
|                           |                                                                           |

### <a name="storage_oneOf_i3"></a>1.4. Property `root > storage > oneOf > tmpfs`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/tmpfs                                                       |
|                           |                                                                           |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date