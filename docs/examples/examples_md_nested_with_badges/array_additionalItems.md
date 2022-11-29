# Schema Docs

- [1. [Optional] Property root > address](#address-72657373)
- [2. [Optional] Property root > addressLines](#addressLines-696e6573)
- [3. [Optional] Property root > arrayEmpty](#arrayEmpty-6d707479)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A little food fun

<details>
<summary><strong> <a name="address-72657373"></a>1. [Optional] Property root > address</strong>  

</summary>
<blockquote>

|          |         |
| -------- | ------- |
| **Type** | `array` |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | True               |
| **Tuple validation** | See below          |

**Example:** 

```json
[
    1600,
    "Pennsylvania",
    "Avenue",
    "NW",
    "Washington"
]
```

</blockquote>
</details>

<details>
<summary><strong> <a name="addressLines-696e6573"></a>2. [Optional] Property root > addressLines</strong>  

</summary>
<blockquote>

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** list of address lines

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
<summary><strong> <a name="arrayEmpty-6d707479"></a>3. [Optional] Property root > arrayEmpty</strong>  

</summary>
<blockquote>

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** This is not a valid JSON Schema, but let's do it anyway.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)