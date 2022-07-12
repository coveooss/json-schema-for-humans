# Person

- [1. [Optional] Property Person > person](#person)
  - [1.1. [Optional] Property Person > person > children](#person_children)
  - [1.2. [Optional] Property Person > person > siblings](#person_siblings)

**Title:** Person

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="person"></a>1. [Optional] Property Person > person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person                                                                                                              |

**Description:** A human being

<details>
<summary><strong> <a name="person_children"></a>1.1. [Optional] Property Person > person > children</strong>  

</summary>
<blockquote>

| Type | `array` |
| ---- | ------- |

**Description:** The children they had

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

</blockquote>
</details>

<details>
<summary><strong> <a name="person_siblings"></a>1.2. [Optional] Property Person > person > siblings</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [person_children_items](#person_children_items)                                                                                   |

**Description:** Person definition from second file. Not the same!

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)