# Person

- [1. [Optional] Property Person > person](#person)
  - [1.1. Person > person > person](#person_items)
    - [1.1.1. [Optional] Property Person > person > items > children](#person_items_children)
      - [1.1.1.1. Person > person > items > children > person](#person_items_children_items)

**Title:** Person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<details>
<summary><strong> <a name="person"></a>1. [Optional] Property Person > person</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** A list of people

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description   |
| ------------------------------- | ------------- |
| [person](#person_items)         | A human being |
|                                 |               |

### <a name="person_items"></a>1.1. Person > person > person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person                                                      |
|                           |                                                                           |

**Description:** A human being

<details>
<summary><strong> <a name="person_items_children"></a>1.1.1. [Optional] Property Person > person > items > children</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The children they had

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be        | Description   |
| -------------------------------------- | ------------- |
| [person](#person_items_children_items) | A human being |
|                                        |               |

##### <a name="person_items_children_items"></a>1.1.1.1. Person > person > items > children > person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [person](#person_items)                                                   |
|                           |                                                                           |

**Description:** A human being

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date