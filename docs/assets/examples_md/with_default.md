# User Preference

- [1. Property `User Preference > favorite_os`](#favorite_os)
- [2. Property `User Preference > favorite_colors`](#favorite_colors)
- [3. Property `User Preference > desired_number_of_shoes`](#desired_number_of_shoes)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [favorite_os](#favorite_os)|No|enum (of string)|No| No|-|
|-  [favorite_colors](#favorite_colors)|No|array of enum (of string)|No| No|-|
|-  [desired_number_of_shoes](#desired_number_of_shoes)|No|integer|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="favorite_os"></a>1. Property `User Preference > favorite_os`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `enum (of string)`
Default: `"Linux"`

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. Property `User Preference > favorite_colors`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `array of enum (of string)`
Default: `["white", "blue"]`

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

## <a name="desired_number_of_shoes"></a>3. Property `User Preference > desired_number_of_shoes`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `integer`
Default: `2`

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |
| **Maximum** | &le; 2 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:28 +0100