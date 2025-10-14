# Schema Docs

- [1. [Required] Propertyroot > outer](#outer)
  - [1.1. [Required] Propertyroot > outer > inner](#outer_inner)
- [2. [Optional] Propertyroot > outer2](#outer2)

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="outer"></a>1. [Required] Propertyroot > outer</strong>  

</summary>
<blockquote>

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | Yes                        |
| **Additional properties** | Not allowed                |
| **Defined in**            | #/definitions/inner schema |

**Description:** We should see this

<details>
<summary>
<strong> <a name="outer_inner"></a>1.1. [Required] Propertyroot > outer > inner</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** inner description

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="outer2"></a>2. [Optional] Propertyroot > outer2</strong>  

</summary>
<blockquote>

|                           |                 |
| ------------------------- | --------------- |
| **Type**                  | `object`        |
| **Required**              | No              |
| **Additional properties** | Not allowed     |
| **Same definition as**    | [outer](#outer) |

**Description:** We should see this too

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)