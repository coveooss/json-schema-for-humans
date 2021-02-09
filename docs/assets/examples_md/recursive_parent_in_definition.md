# Person

- [1. Property `Person > relationships`](#relationships)
  - [1.1. Property `Person > relationships > mother`](#relationships_mother)
    - [1.1.1. Property `Person > relationships > mother > relationships`](#relationships_mother_relationships)
      - [1.1.1.1. Property `Person > relationships > mother > relationships > mother`](#relationships_mother_relationships_mother)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships)|No|Combination|No|No| No|Relationships between this person and others|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="relationships"></a>1. Property `Person > relationships`

Type: `object`

**Description:** <p>Relationships between this person and others</p>

Defined in: #/definitions/person/properties/relationships

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother)|No|Combination|No|No| No|A human being|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="relationships_mother"></a>1.1. Property `Person > relationships > mother`

Type: `object`

**Description:** <p>A human being</p>

Defined in: #/definitions/person

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships_mother_relationships)|No|Combination|No|No| No|Relationships between this person and others|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

#### <a name="relationships_mother_relationships"></a>1.1.1. Property `Person > relationships > mother > relationships`

Type: `object`

**Description:** <p>Relationships between this person and others</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother_relationships_mother)|No|Combination|No|No| No|A human being|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

##### <a name="relationships_mother_relationships_mother"></a>1.1.1.1. Property `Person > relationships > mother > relationships > mother`

Type: `object`

**Description:** <p>A human being</p>

Same definition as [mother](#relationships_mother)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:35 +0100