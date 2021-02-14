# User Preference

- [1. [Optional] Property `User Preference > favorite_os`](#favorite_os)
- [2. [Optional] Property `User Preference > favorite_colors`](#favorite_colors)
- [3. [Optional] Property `User Preference > desired_number_of_shoes`](#desired_number_of_shoes)

**Title:** User Preference

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Property                                               | Pattern | Type                      | Deprecated | Definition | Title/Description |
| ------------------------------------------------------ | ------- | ------------------------- | ---------- | ---------- | ----------------- |
| - [favorite_os](#favorite_os )                         | No      | enum (of string)          | No         | -          | -                 |
| - [favorite_colors](#favorite_colors )                 | No      | array of enum (of string) | No         | -          | -                 |
| - [desired_number_of_shoes](#desired_number_of_shoes ) | No      | integer                   | No         | -          | -                 |
|                                                        |         |                           |            |            |                   |

## <a name="favorite_os"></a>1. [Optional] Property `User Preference > favorite_os`

| Type                      | `enum (of string)`                                                        |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Linux"`                                                                 |
|                           |                                                                           |

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. [Optional] Property `User Preference > favorite_colors`

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
| **Tuple validation** | N/A                |
|                      |                    |

## <a name="desired_number_of_shoes"></a>3. [Optional] Property `User Preference > desired_number_of_shoes`

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-14 at 10:29:44 +0100