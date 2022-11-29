# Schema Docs

- [1. [Required] Property root > storage](#storage-72616765)
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

<details>
<summary><strong> <a name="storage-72616765"></a>1. [Required] Property root > storage</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<blockquote>

| Any of(Option)                           |
| ---------------------------------------- |
| [diskDevice](#storage_anyOf_i0-665f6930) |
| [diskUUID](#storage_anyOf_i1-665f6931)   |
| [item 2](#storage_anyOf_i2-665f6932)     |
| [tmpfs](#storage_anyOf_i3-665f6933)      |

<blockquote>

### <a name="storage_anyOf_i0-665f6930"></a>1.1. Property `root > storage > anyOf > diskDevice`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskDevice                                                  |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i1-665f6931"></a>1.2. Property `root > storage > anyOf > diskUUID`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskUUID                                                    |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i2-665f6932"></a>1.3. Property `root > storage > anyOf > item 2`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i3-665f6933"></a>1.4. Property `root > storage > anyOf > tmpfs`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/tmpfs                                                       |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)