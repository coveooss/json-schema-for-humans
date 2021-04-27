# Person

**Title:** Person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<details>
<summary><strong> <a name="person"></a>[Optional] Property person</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** A list of people

| Each item of this array must be | Description   |
| ------------------------------- | ------------- |
| [person](#person_items)         | A human being |
|                                 |               |

### <a name="person_items"></a>person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person                                                      |
|                           |                                                                           |

**Description:** A human being

<details>
<summary><strong> <a name="person_items_children"></a>[Optional] Property children</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The children they had

| Each item of this array must be        | Description   |
| -------------------------------------- | ------------- |
| [person](#person_items_children_items) | A human being |
|                                        |               |

##### <a name="person_items_children_items"></a>person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[person](#person_items)`                                                 |
|                           |                                                                           |

**Description:** A human being

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date