# Schema Docs

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > fruits`](#fruits)
  - [1.1. root > fruits > items](#autogenerated_heading_2)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > vegetables`](#vegetables)
  - [2.1. root > vegetables > veggie](#autogenerated_heading_3)
    - [2.1.1. Property `root > vegetables > items > veggieName`](#vegetables_items_veggieName)
    - [2.1.2. Property `root > vegetables > items > veggieLike`](#vegetables_items_veggieLike)

| Type                      | `object`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

**Description:** A schema with an array

| Property                     | Pattern | Type            | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [fruits](#fruits )         | No      | array of string | No         | -          | -                 |
| - [vegetables](#vegetables ) | No      | array           | No         | -          | -                 |
|                              |         |                 |            |            |                   |

## <a name="fruits"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > fruits`

| Type                      | `array of string`                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
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
| [items](#fruits_items)          | -           |
|                                 |             |

### <a name="autogenerated_heading_2"></a>1.1. root > fruits > items

| Type                      | `string`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

## <a name="vegetables"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > vegetables`

| Type                      | `array`                                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
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
| [veggie](#vegetables_items)     | -           |
|                                 |             |

### <a name="autogenerated_heading_3"></a>2.1. root > vegetables > veggie

| Type                      | `object`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/veggie                                                                                                 |
|                           |                                                                                                                      |

| Property                                      | Pattern | Type    | Deprecated | Definition | Title/Description          |
| --------------------------------------------- | ------- | ------- | ---------- | ---------- | -------------------------- |
| + [veggieName](#vegetables_items_veggieName ) | No      | string  | No         | -          | The name of the vegetable. |
| + [veggieLike](#vegetables_items_veggieLike ) | No      | boolean | No         | -          | Do I like this vegetable?  |
|                                               |         |         |            |            |                            |

#### <a name="vegetables_items_veggieName"></a>2.1.1. Property `root > vegetables > items > veggieName`

| Type                      | `string`                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

**Description:** The name of the vegetable.

#### <a name="vegetables_items_veggieLike"></a>2.1.2. Property `root > vegetables > items > veggieLike`

| Type                      | `boolean`                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type--allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                      |

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-14 at 22:41:50 +0100