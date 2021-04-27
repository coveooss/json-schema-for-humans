# Circular reference Schema

**Title:** Circular reference Schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<details>
<summary><strong> <a name="person"></a>[Optional] Property person</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/a                                                           |
|                           |                                                                           |

<details>
<summary><strong> <a name="person_a1"></a>[Optional] Property a1</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from c"`                                                        |
| **Defined in**            | #/definitions/b                                                           |
|                           |                                                                           |

**Description:** Description from b

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date