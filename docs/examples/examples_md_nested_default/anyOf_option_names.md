# Schema Docs

- [1. [Required] Property root > storage](#storage)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage_anyOf_i0)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage_anyOf_i1)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage_anyOf_i2)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage_anyOf_i3)

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** JSON Schema for an fstab entry

<details>
<summary><strong> <a name="storage"></a>1. [Required] Property root > storage</strong>  

</summary>
<blockquote>

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<blockquote>

| Any of(Option)                  |
| ------------------------------- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1)   |
| [item 2](#storage_anyOf_i2)     |
| [tmpfs](#storage_anyOf_i3)      |
|                                 |

<blockquote>

### <a name="storage_anyOf_i0"></a>1.1. Property `root > storage > anyOf > diskDevice`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskDevice                                                  |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i1"></a>1.2. Property `root > storage > anyOf > diskUUID`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskUUID                                                    |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i2"></a>1.3. Property `root > storage > anyOf > item 2`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i3"></a>1.4. Property `root > storage > anyOf > tmpfs`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/tmpfs                                                       |
|                           |                                                                           |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date