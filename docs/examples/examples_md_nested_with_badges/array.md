# Schema Docs

- [1. [Optional] Property root > fruits](#fruits)
  - [1.1. root > fruits > items](#fruits_items)
- [2. [Optional] Property root > vegetables](#vegetables)
  - [2.1. root > vegetables > veggie](#vegetables_items)
    - [2.1.1. [Required] Property root > vegetables > items > veggieName](#vegetables_items_veggieName)
    - [2.1.2. [Required] Property root > vegetables > items > veggieLike](#vegetables_items_veggieLike)

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** A schema with an array

<details>
<summary><strong> <a name="fruits"></a>1. [Optional] Property root > fruits</strong>  

</summary>
<blockquote>

| Type                      | `array of string`                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#fruits_items)          | -           |
|                                 |             |

### <a name="fruits_items"></a>1.1. root > fruits > items

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="vegetables"></a>2. [Optional] Property root > vegetables</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [veggie](#vegetables_items)     | -           |
|                                 |             |

### <a name="vegetables_items"></a>2.1. root > vegetables > veggie

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/veggie                                                                                                |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="vegetables_items_veggieName"></a>2.1.1. [Required] Property root > vegetables > items > veggieName</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The name of the vegetable.

</blockquote>
</details>

<details>
<summary><strong> <a name="vegetables_items_veggieLike"></a>2.1.2. [Required] Property root > vegetables > items > veggieLike</strong>  

</summary>
<blockquote>

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Do I like this vegetable?

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date