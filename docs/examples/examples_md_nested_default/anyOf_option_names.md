# Schema Docs

- [1. [Required] Propertyroot > storage](#storage)
  - [1.1. Property `root > storage > anyOf > diskDevice`](#storage_anyOf_i0)
  - [1.2. Property `root > storage > anyOf > diskUUID`](#storage_anyOf_i1)
  - [1.3. Property `root > storage > anyOf > item 2`](#storage_anyOf_i2)
  - [1.4. Property `root > storage > anyOf > tmpfs`](#storage_anyOf_i3)

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Description:** JSON Schema for an fstab entry

<details>
<summary>
<strong> <a name="storage"></a>1. [Required] Propertyroot > storage</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | Yes         |

<blockquote>

| Any of(Option)                  |
| ------------------------------- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1)   |
| [item 2](#storage_anyOf_i2)     |
| [tmpfs](#storage_anyOf_i3)      |

<blockquote>

### <a name="storage_anyOf_i0"></a>1.1. Property `root > storage > anyOf > diskDevice`

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `object`                 |
| **Required**   | No                       |
| **Defined in** | #/definitions/diskDevice |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i1"></a>1.2. Property `root > storage > anyOf > diskUUID`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `object`               |
| **Required**   | No                     |
| **Defined in** | #/definitions/diskUUID |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i2"></a>1.3. Property `root > storage > anyOf > item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

</blockquote>
<blockquote>

### <a name="storage_anyOf_i3"></a>1.4. Property `root > storage > anyOf > tmpfs`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `object`            |
| **Required**   | No                  |
| **Defined in** | #/definitions/tmpfs |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)