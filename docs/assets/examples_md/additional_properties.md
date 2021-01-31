# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subType1](#subType1)|No|object|No|No| No|A sub type with additionalProperties false.|
| [subType2](#subType2)|No|object|No|No| No|A sub type with additionalProperties true.|
| [additionalProperties](#additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Should-conform-blue)](# "Each additional property must conform to the following schema")|additionalProperties schema.|

## <a name="subType1"></a> 1. Property `subType1`

**Description**:  A sub type with additionalProperties false.

      Person
 >   subType1

Type: `object`

**Description:** A sub type with additionalProperties false.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|subProp1|No|number|No|No| No||
`No Additional Properties`

## <a name="subType2"></a> 2. Property `subType2`

**Description**:  A sub type with additionalProperties true.

      Person
 >   subType2

Type: `object`

**Description:** A sub type with additionalProperties true.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|subProp2|No|number|No|No| No||
| [additionalProperties](#subType2_additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Any%20type+allowed-green)](# "Additional Properties of any type are allowed.")||

### <a name="subType2_additionalProperties"></a> 2.1. Property `additionalProperties`

      Person
 >   subType2
 >   additionalProperties

Type: `object`

## <a name="additionalProperties"></a> 3. Property `additionalProperties`

**Description**:  additionalProperties schema.

      Person
 >   additionalProperties

Type: `object`

**Description:** additionalProperties schema.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|propA|No|number|No|No| No||

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:00:08 +0100