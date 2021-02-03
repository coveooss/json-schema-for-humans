

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships)|No|object|No|No| No|Relationships between this person and others|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="relationships"></a>1.  Property `Person > relationships`

Type: `object`

**Description:** Relationships between this person and others
Defined in: #/definitions/person/properties/relationships

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother)|No|object|No|No| No|A human being|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="relationships_mother"></a>1.1.  Property `Person > relationships > mother`

Type: `object`

**Description:** A human being
Defined in: #/definitions/person

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships_mother_relationships)|No|object|No|No| No|Relationships between this person and others|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

####  <a name="relationships_mother_relationships"></a>1.1.1.  Property `Person > relationships > mother > relationships`

Type: `object`

**Description:** Relationships between this person and others

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother_relationships_mother)|No|object|No|No| No|A human being|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

#####  <a name="relationships_mother_relationships_mother"></a>1.1.1.1.  Property `Person > relationships > mother > relationships > mother`

Type: `object`

**Description:** A human being
    Same definition as [mother](#relationships_mother)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:48 +0100