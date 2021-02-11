# Person

- [1. Property `Person > subType1`](#subType1)
  - [1.1. Property `Person > subType1 > subProp1`](#subType1_subProp1)
- [2. Property `Person > subType2`](#subType2)
  - [2.1. Property `Person > subType2 > subProp2`](#subType2_subProp2)
- [3. Property `Person > additionalProperties`](#additionalProperties)
  - [3.1. Property `Person > additionalProperties > propA`](#additionalProperties_propA)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [subType1](#subType1)|No|object|No| No|A sub type with additionalProperties false.|
| [subType2](#subType2)|No|object|No| No|A sub type with additionalProperties true.|
| [additionalProperties](#additionalProperties)|No|object|No|  [![made-with-Markdown](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema")|additionalProperties schema.|

## <a name="subType1"></a>1. Property `Person > subType1`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** A sub type with additionalProperties false.

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [subProp1](#subType1_subProp1)|No|number|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

### <a name="subType1_subProp1"></a>1.1. Property `Person > subType1 > subProp1`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `number`

## <a name="subType2"></a>2. Property `Person > subType2`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** A sub type with additionalProperties true.

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [subProp2](#subType2_subProp2)|No|number|No| No|-|
| [additionalProperties](#subType2_additionalProperties)|No|object|No|  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|-|

### <a name="subType2_subProp2"></a>2.1. Property `Person > subType2 > subProp2`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `number`

## <a name="additionalProperties"></a>3. Property `Person > additionalProperties`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** additionalProperties schema.

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [propA](#additionalProperties_propA)|No|number|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="additionalProperties_propA"></a>3.1. Property `Person > additionalProperties > propA`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `number`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:07 +0100