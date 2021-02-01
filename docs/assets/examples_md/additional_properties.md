

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subType1](#subType1)|No|object|No|No| No|A sub type with additionalProperties false.|| [subType2](#subType2)|No|object|No|No| No|A sub type with additionalProperties true.|| [additionalProperties](#additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Should-conform-blue)](# "Each additional property must conform to the following schema")|additionalProperties schema.|

##  <a name="subType1"></a>1.  Property `Person > subType1`

**Description**:  A sub type with additionalProperties false.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp1](#subType1_subProp1)|No|number|No|No| No||`No Additional Properties`

###  <a name="subType1_subProp1"></a>1.1.  Property `Person > subType1 > subProp1`

##  <a name="subType2"></a>2.  Property `Person > subType2`

**Description**:  A sub type with additionalProperties true.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp2](#subType2_subProp2)|No|number|No|No| No||| [additionalProperties](#subType2_additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")||

###  <a name="subType2_subProp2"></a>2.1.  Property `Person > subType2 > subProp2`

###  <a name="subType2_additionalProperties"></a>2.2.  Property `Person > subType2 > additionalProperties`

##  <a name="additionalProperties"></a>3.  Property `Person > additionalProperties`

**Description**:  additionalProperties schema.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propA](#additionalProperties_propA)|No|number|No|No| No||

###  <a name="additionalProperties_propA"></a>3.1.  Property `Person > additionalProperties > propA`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 00:44:57 +0100