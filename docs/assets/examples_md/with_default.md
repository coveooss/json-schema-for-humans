# User Preference

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_os`](#favorite_os)
- [2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_colors`](#favorite_colors)
- [3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > desired_number_of_shoes`](#desired_number_of_shoes)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [favorite_os](#favorite_os)|No|enum (of string)|No|-|
|-  [favorite_colors](#favorite_colors)|No|array of enum (of string)|No|-|
|-  [desired_number_of_shoes](#desired_number_of_shoes)|No|integer|No|-|

## <a name="favorite_os"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_os`

| Type | `enum (of string)` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `"Linux"` |

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > favorite_colors`

| Type | `array of enum (of string)` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `["white", "blue"]` |

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

## <a name="desired_number_of_shoes"></a>3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `User Preference > desired_number_of_shoes`

| Type | `integer` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `2` |

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |
| **Maximum** | &le; 2 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 22:25:43 +0100