# Schema Docs

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** A schema with an array

<details>
<summary><strong> <a name="fruits"></a>[Optional] Property fruits</strong>  

</summary>
<blockquote>

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#fruits_items)          | -           |
|                                 |             |

### <a name="fruits_items"></a>items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="vegetables"></a>[Optional] Property vegetables</strong>  

</summary>
<blockquote>

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [veggie](#vegetables_items)     | -           |
|                                 |             |

### <a name="vegetables_items"></a>veggie

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/veggie                                                      |
|                           |                                                                           |

<details>
<summary><strong> <a name="vegetables_items_veggieName"></a>[Required] Property veggieName</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The name of the vegetable.

</blockquote>
</details>

<details>
<summary><strong> <a name="vegetables_items_veggieLike"></a>[Required] Property veggieLike</strong>  

</summary>
<blockquote>

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Do I like this vegetable?

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date