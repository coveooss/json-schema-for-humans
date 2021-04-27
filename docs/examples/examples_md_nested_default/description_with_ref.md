# Schema Docs

- [1. [Required] Property root > outer](#outer)
  - [1.1. [Required] Property root > outer > inner](#outer_inner)
- [2. [Optional] Property root > outer2](#outer2)

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
|                           |                                                         |

<details>
<summary><strong> <a name="outer"></a>1. [Required] Property root > outer</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/inner schema                                                |
|                           |                                                                           |

**Description:** We should see this

<details>
<summary><strong> <a name="outer_inner"></a>1.1. [Required] Property root > outer > inner</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** inner description

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="outer2"></a>2. [Optional] Property root > outer2</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[outer](#outer)`                                                         |
|                           |                                                                           |

**Description:** We should see this too

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date