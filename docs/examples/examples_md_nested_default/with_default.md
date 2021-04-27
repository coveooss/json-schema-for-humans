# User Preference

- [1. [Optional] Property User Preference > favorite_os](#favorite_os)
- [2. [Optional] Property User Preference > favorite_colors](#favorite_colors)
  - [2.1. User Preference > favorite_colors > items](#favorite_colors_items)
- [3. [Optional] Property User Preference > desired_number_of_shoes](#desired_number_of_shoes)

**Title:** User Preference

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

<details>
<summary><strong> <a name="favorite_os"></a>1. [Optional] Property User Preference > favorite_os</strong>  

</summary>
<blockquote>

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Linux"`                                                                 |
|                           |                                                                           |

Must be one of:
* "Windows"
* "Mac"
* "Linux"

</blockquote>
</details>

<details>
<summary><strong> <a name="favorite_colors"></a>2. [Optional] Property User Preference > favorite_colors</strong>  

</summary>
<blockquote>

| Type                      | `array of enum (of string)`                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `["white", "blue"]`                                                       |
|                           |                                                                           |

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
| [items](#favorite_colors_items) | -           |
|                                 |             |

### <a name="favorite_colors_items"></a>2.1. User Preference > favorite_colors > items

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

Must be one of:
* "green"
* "blue"
* "orange"
* "red"
* "white"
* "black"

</blockquote>
</details>

<details>
<summary><strong> <a name="desired_number_of_shoes"></a>3. [Optional] Property User Preference > desired_number_of_shoes</strong>  

</summary>
<blockquote>

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `2`                                                                       |
|                           |                                                                           |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 2 |
|              |        |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date