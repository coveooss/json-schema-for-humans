# Person

- [1. Property `Person > subType1`](#subType1)
  - [1.1. Property `Person > subType1 > subProp1`](#subType1_subProp1)
- [2. Property `Person > subType2`](#subType2)
  - [2.1. Property `Person > subType2 > subProp2`](#subType2_subProp2)
- [3. Property `Person > anInt`](#anInt)
- [4. Property `Person > additionalProperties`](#additionalProperties)
  - [4.1. Property `Person > additionalProperties > propA`](#additionalProperties_propA)

**Title:** Person

|                           |                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                  |
| **Required**              | No                                                                                                        |
| **Additional properties** | [[Should-conform]](#additionalProperties "Each additional property must conform to the following schema") |

| Property                                         | Pattern | Type    | Deprecated | Definition | Title/Description                                                          |
| ------------------------------------------------ | ------- | ------- | ---------- | ---------- | -------------------------------------------------------------------------- |
| - [subType1](#subType1 )                         | No      | object  | No         | -          | A sub type with additionalProperties false.                                |
| - [subType2](#subType2 )                         | No      | object  | No         | -          | A sub type with additionalProperties true.                                 |
| - [anInt](#anInt )                               | No      | integer | No         | -          | This is an integer, it should not show additional properties. (issue #132) |
| - [additionalProperties](#additionalProperties ) | No      | object  | No         | -          | additionalProperties schema.                                               |

## <a name="subType1"></a>1. Property `Person > subType1`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** A sub type with additionalProperties false.

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp1](#subType1_subProp1 ) | No      | number | No         | -          | -                 |

### <a name="subType1_subProp1"></a>1.1. Property `Person > subType1 > subProp1`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="subType2"></a>2. Property `Person > subType2`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A sub type with additionalProperties true.

| Property                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [subProp2](#subType2_subProp2 )                         | No      | number | No         | -          | -                 |
| - [additionalProperties](#subType2_additionalProperties ) | No      | object | No         | -          | -                 |

### <a name="subType2_subProp2"></a>2.1. Property `Person > subType2 > subProp2`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="anInt"></a>3. Property `Person > anInt`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** This is an integer, it should not show additional properties. (issue #132)

## <a name="additionalProperties"></a>4. Property `Person > additionalProperties`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** additionalProperties schema.

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [propA](#additionalProperties_propA ) | No      | number | No         | -          | -                 |

### <a name="additionalProperties_propA"></a>4.1. Property `Person > additionalProperties > propA`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
