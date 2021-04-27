# Person

**Title:** Person

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="person"></a>[Optional] Property person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person                                                                                                |
|                           |                                                                                                                     |

**Description:** A human being

<details>
<summary><strong> <a name="person_children"></a>[Optional] Property children</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The children they had

| Each item of this array must be  | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| [person](#person_children_items) | Person definition from second file. Not the same! |
|                                  |                                                   |

#### <a name="person_children_items"></a>person

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[siblings](#person_siblings)`                                                                                      |
|                           |                                                                                                                     |

**Description:** Person definition from second file. Not the same!

</blockquote>
</details>

<details>
<summary><strong> <a name="person_siblings"></a>[Optional] Property siblings</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | recursive_two_files2.json#/definitions/person                                                                       |
|                           |                                                                                                                     |

**Description:** Person definition from second file. Not the same!

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date