# Schema Docs

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Testing $ref

<details>
<summary><strong> <a name="a_gift"></a>[Optional] Property a_gift</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                        |
|                           |                                                                           |

**Description:** A gift, or is it?

</blockquote>
</details>

<details>
<summary><strong> <a name="anchor_with_slash"></a>[Optional] Property anchor_with_slash</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/object_def                                                  |
|                           |                                                                           |

<details>
<summary><strong> <a name="anchor_with_slash_propertyA"></a>[Optional] Property propertyA</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Description for object_def/items/propertyA

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="anchor_no_slash"></a>[Optional] Property anchor_no_slash</strong>  

</summary>
<blockquote>

| Type                      | `array of string`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #definitions/array_def                                                    |
|                           |                                                                           |

**Description:** Description for array_def

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#anchor_no_slash_items) | -           |
|                                 |             |

### <a name="anchor_no_slash_items"></a>items

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="anchor_nested_reference"></a>[Optional] Property anchor_nested_reference</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/reference_def                                               |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="same_file_anchor_with_slash"></a>[Optional] Property same_file_anchor_with_slash</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | references.json#/definitions/string_def                                   |
|                           |                                                                           |

**Description:** Description for string_def

</blockquote>
</details>

<details>
<summary><strong> <a name="same_file_anchor_no_slash"></a>[Optional] Property same_file_anchor_no_slash</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[anchor_with_slash](#anchor_with_slash)`                                 |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="same_file_nested_reference"></a>[Optional] Property same_file_nested_reference</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[anchor_nested_reference](#anchor_nested_reference)`                     |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="other_file_anchor"></a>[Optional] Property other_file_anchor</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | with_descriptions.json#/definitions/gift                                  |
|                           |                                                                           |

**Description:** The delivery is a gift, no prices displayed

<details>
<summary><strong> <a name="other_file_anchor_with_wrap"></a>[Optional] Property with_wrap</strong>  

</summary>
<blockquote>

| Type                      | `boolean`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="other_file_dot_anchor"></a>[Optional] Property other_file_dot_anchor</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[other_file_anchor](#other_file_anchor)`                                 |
|                           |                                                                           |

**Description:** The delivery is a gift, no prices displayed

</blockquote>
</details>

<details>
<summary><strong> <a name="other_file_dot_dot_anchor"></a>[Optional] Property other_file_dot_dot_anchor</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[other_file_anchor](#other_file_anchor)`                                 |
|                           |                                                                           |

**Description:** The delivery is a gift, no prices displayed

</blockquote>
</details>

<details>
<summary><strong> <a name="other_file_only"></a>[Optional] Property other_file_only</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | combining_not.json                                                        |
|                           |                                                                           |

**Description:** Test schema with a not

<details>
<summary><strong> <a name="other_file_only_not_a_string"></a>[Required] Property not_a_string</strong>  

</summary>
<blockquote>

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

#### <a name="autogenerated_heading_2"></a>Must **not** be

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="multi_hierarchy_reference"></a>[Optional] Property multi_hierarchy_reference</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | reference_schemas/intermediate.json#/properties/cross_file_reference      |
|                           |                                                                           |

<details>
<summary><strong> <a name="multi_hierarchy_reference_propertyA"></a>[Optional] Property propertyA</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Contents of propertyA in final.json

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date