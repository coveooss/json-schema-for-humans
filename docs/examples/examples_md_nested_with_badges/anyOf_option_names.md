# Schema Docs

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** JSON Schema for an fstab entry

<details>
<summary><strong> <a name="storage"></a>[Required] Property storage</strong>  

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

### <a name="storage_anyOf_i0"></a>Property `diskDevice`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskDevice                                                  |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i1"></a>Property `diskUUID`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/diskUUID                                                    |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i2"></a>Property `item 2`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i3"></a>Property `tmpfs`

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