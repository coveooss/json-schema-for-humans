# Person

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1`](#subType1-79706531)
  - [1.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1 > subProp1`](#subType1_subProp1-726f7031)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2`](#subType2-79706532)
  - [2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2 > subProp2`](#subType2_subProp2-726f7032)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > anInt`](#anInt-6e496e74)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties`](#additionalProperties-74696573)
  - [4.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties > propA`](#additionalProperties_propA-726f7041)

**Title:** Person

|                           |                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                                                              |
| **Additional properties** | [![Should-conform](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties-74696573 "Each additional property must conform to the following schema") |

| Property                                                  | Pattern | Type    | Deprecated | Definition | Title/Description                                                          |
| --------------------------------------------------------- | ------- | ------- | ---------- | ---------- | -------------------------------------------------------------------------- |
| - [subType1](#subType1-79706531 )                         | No      | object  | No         | -          | A sub type with additionalProperties false.                                |
| - [subType2](#subType2-79706532 )                         | No      | object  | No         | -          | A sub type with additionalProperties true.                                 |
| - [anInt](#anInt-6e496e74 )                               | No      | integer | No         | -          | This is an integer, it should not show additional properties. (issue #132) |
| - [additionalProperties](#additionalProperties-74696573 ) | No      | object  | No         | -          | additionalProperties schema.                                               |

## <a name="subType1-79706531"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp1](#subType1_subProp1-726f7031 ) | No      | number | No         | -          | -                 |

### <a name="subType1_subProp1-726f7031"></a>1.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType1 > subProp1`

|          |          |
| -------- | -------- |
| **Type** | `number` |

## <a name="subType2-79706532"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

| Property                                                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp2](#subType2_subProp2-726f7032 )                         | No      | number | No         | -          | -                 |
| - [additionalProperties](#subType2_additionalProperties-74696573 ) | No      | object | No         | -          | -                 |

### <a name="subType2_subProp2-726f7032"></a>2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > subType2 > subProp2`

|          |          |
| -------- | -------- |
| **Type** | `number` |

## <a name="anInt-6e496e74"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > anInt`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** This is an integer, it should not show additional properties. (issue #132)

## <a name="additionalProperties-74696573"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

| Property                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [propA](#additionalProperties_propA-726f7041 ) | No      | number | No         | -          | -                 |

### <a name="additionalProperties_propA-726f7041"></a>4.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > additionalProperties > propA`

|          |          |
| -------- | -------- |
| **Type** | `number` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
