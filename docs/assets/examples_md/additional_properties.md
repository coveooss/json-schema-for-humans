# Person

- [1. Property `Person > subType1`](#subType1)
  - [1.1. Property `Person > subType1 > subProp1`](#subType1_subProp1)
- [2. Property `Person > subType2`](#subType2)
  - [2.1. Property `Person > subType2 > subProp2`](#subType2_subProp2)
- [3. Property `Person > additionalProperties`](#additionalProperties)
  - [3.1. Property `Person > additionalProperties > propA`](#additionalProperties_propA)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subType1](#subType1)|No|object|No|No| No|A sub type with additionalProperties false.|
| [subType2](#subType2)|No|object|No|No| No|A sub type with additionalProperties true.|
| [additionalProperties](#additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema")|additionalProperties schema.|

## <a name="subType1"></a>1. Property `Person > subType1`

Type: `object`

**Description:** <p>A sub type with additionalProperties false.</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp1](#subType1_subProp1)|No|number|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

### <a name="subType1_subProp1"></a>1.1. Property `Person > subType1 > subProp1`

Type: `number`

## <a name="subType2"></a>2. Property `Person > subType2`

Type: `object`

**Description:** <p>A sub type with additionalProperties true.</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp2](#subType2_subProp2)|No|number|No|No| No|-|
| [additionalProperties](#subType2_additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|-|

### <a name="subType2_subProp2"></a>2.1. Property `Person > subType2 > subProp2`

Type: `number`

## <a name="additionalProperties"></a>3. Property `Person > additionalProperties`

Type: `object`

**Description:** <p>additionalProperties schema.</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propA](#additionalProperties_propA)|No|number|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="additionalProperties_propA"></a>3.1. Property `Person > additionalProperties > propA`

Type: `number`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 22:03:56 +0100