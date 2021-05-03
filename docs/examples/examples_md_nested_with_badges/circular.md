# Circular reference Schema

- [1. [Optional] Property Circular reference Schema > person](#person)
  - [1.1. [Optional] Property Circular reference Schema > person > a1](#person_a1)

**Title:** Circular reference Schema

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="person"></a>1. [Optional] Property Circular reference Schema > person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/a                                                                                                     |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="person_a1"></a>1.1. [Optional] Property Circular reference Schema > person > a1</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from c"`                                                                                                  |
| **Defined in**            | #/definitions/b                                                                                                     |
|                           |                                                                                                                     |

**Description:** Description from b

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date