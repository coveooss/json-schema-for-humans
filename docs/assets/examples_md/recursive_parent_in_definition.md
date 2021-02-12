# Person

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships`](#relationships)
  - [1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother`](#relationships_mother)
    - [1.1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother > relationships`](#relationships_mother_relationships)
      - [1.1.1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother > relationships > mother`](#relationships_mother_relationships_mother)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [relationships](#relationships)|No|object|No|Relationships between this person and others|
|  |  |  |  |  |

## <a name="relationships"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/person/properties/relationships |
|  |  |

**Description:** Relationships between this person and others

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [mother](#relationships_mother)|No|object|No|A human being|
|  |  |  |  |  |

### <a name="relationships_mother"></a>1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/person |
|  |  |

**Description:** A human being

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [relationships](#relationships_mother_relationships)|No|object|No|Relationships between this person and others|
|  |  |  |  |  |

#### <a name="relationships_mother_relationships"></a>1.1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother > relationships`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Relationships between this person and others

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [mother](#relationships_mother_relationships_mother)|No|object|No|A human being|
|  |  |  |  |  |

##### <a name="relationships_mother_relationships_mother"></a>1.1.1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > relationships > mother > relationships > mother`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Same definition as** | [mother](#relationships_mother) |
|  |  |

**Description:** A human being

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:56:20 +0100