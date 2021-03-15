# Person

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1`](#subType1)
  - [1.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1 > subProp1`](#subType1_subProp1)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2`](#subType2)
  - [2.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2 > subProp2`](#subType2_subProp2)
- [3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties`](#additionalProperties)
  - [3.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties > propA`](#additionalProperties_propA)

**Title:** Person

| Type                      | `object`                                                                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema") |
|                           |                                                                                                                                                     |

| Property                                         | Pattern | Type   | Deprecated | Definition | Title/Description                           |
| ------------------------------------------------ | ------- | ------ | ---------- | ---------- | ------------------------------------------- |
| - [subType1](#subType1 )                         | No      | object | No         | -          | A sub type with additionalProperties false. |
| - [subType2](#subType2 )                         | No      | object | No         | -          | A sub type with additionalProperties true.  |
| - [additionalProperties](#additionalProperties ) | No      | object | No         | -          | additionalProperties schema.                |
|                                                  |         |        |            |            |                                             |

## <a name="subType1"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1`

| Type                      | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | [![badge](https://img.shields.io/badge/Not+allowed-red)](# "Additional Properties not allowed.") |
|                           |                                                                                                  |

**Description:** A sub type with additionalProperties false.

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp1](#subType1_subProp1 ) | No      | number | No         | -          | -                 |
|                                   |         |        |            |            |                   |

### <a name="subType1_subProp1"></a>1.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1 > subProp1`

| Type                      | `number`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

## <a name="subType2"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** A sub type with additionalProperties true.

| Property                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp2](#subType2_subProp2 )                         | No      | number | No         | -          | -                 |
| - [additionalProperties](#subType2_additionalProperties ) | No      | object | No         | -          | -                 |
|                                                           |         |        |            |            |                   |

### <a name="subType2_subProp2"></a>2.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2 > subProp2`

| Type                      | `number`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

## <a name="additionalProperties"></a>3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** additionalProperties schema.

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [propA](#additionalProperties_propA ) | No      | number | No         | -          | -                 |
|                                         |         |        |            |            |                   |

### <a name="additionalProperties_propA"></a>3.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties > propA`

| Type                      | `number`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date