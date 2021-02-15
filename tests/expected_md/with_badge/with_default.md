# User Preference

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_os`](#favorite_os)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_colors`](#favorite_colors)
  - [2.1. User Preference > favorite_colors > items](#autogenerated_heading_2)
- [3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > desired_number_of_shoes`](#desired_number_of_shoes)

**Title:** User Preference

| Type                      | `object`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

| Property                                               | Pattern | Type                      | Deprecated | Definition | Title/Description |
| ------------------------------------------------------ | ------- | ------------------------- | ---------- | ---------- | ----------------- |
| - [favorite_os](#favorite_os )                         | No      | enum (of string)          | No         | -          | -                 |
| - [favorite_colors](#favorite_colors )                 | No      | array of enum (of string) | No         | -          | -                 |
| - [desired_number_of_shoes](#desired_number_of_shoes ) | No      | integer                   | No         | -          | -                 |
|                                                        |         |                           |            |            |                   |

## <a name="favorite_os"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_os`

| Type                      | `enum (of string)`                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Linux"`                                                                                                            |
|                           |                                                                                                                      |

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_colors`

| Type                      | `array of enum (of string)`                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `["white", "blue"]`                                                                                                  |
|                           |                                                                                                                      |

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

### <a name="autogenerated_heading_2"></a>2.1. User Preference > favorite_colors > items

| Type                      | `enum (of string)`                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

Must be one of:
* "green"
* "blue"
* "orange"
* "red"
* "white"
* "black"

## <a name="desired_number_of_shoes"></a>3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `User Preference > desired_number_of_shoes`

| Type                      | `integer`                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `2`                                                                                                                  |
|                           |                                                                                                                      |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 2 |
|              |        |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-14 at 22:41:48 +0100