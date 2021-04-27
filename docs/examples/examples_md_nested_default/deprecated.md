# Schema Docs

- [1. [Optional]~~ Property root > deprecated1~~](#deprecated1)
- [2. [Optional]~~ Property root > deprecated2~~](#deprecated2)
- [3. [Optional] Property root > not_deprecated](#not_deprecated)

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Test schema with deprecated in description

<details>
<summary><strong> <a name="deprecated1"></a>1. [Optional]~~ Property root > deprecated1~~</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** [Deprecated]

</blockquote>
</details>

<details>
<summary><strong> <a name="deprecated2"></a>2. [Optional]~~ Property root > deprecated2~~</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** [Deprecated - Use `not_deprecated` instead]

</blockquote>
</details>

<details>
<summary><strong> <a name="not_deprecated"></a>3. [Optional] Property root > not_deprecated</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date