# Person

- [1. Property `Person > relationships`](#relationships)
  - [1.1. Property `Person > relationships > mother`](#relationships_mother)
    - [1.1.1. Property `Person > relationships > mother > relationships`](#relationships_mother_relationships)
      - [1.1.1.1. Property `Person > relationships > mother > relationships > mother`](#relationships_mother_relationships_mother)

**Title:** Person

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                           | Pattern | Type   | Deprecated | Definition                                       | Title/Description                            |
| ---------------------------------- | ------- | ------ | ---------- | ------------------------------------------------ | -------------------------------------------- |
| - [relationships](#relationships ) | No      | object | No         | In #/definitions/person/properties/relationships | Relationships between this person and others |

## <a name="relationships"></a>1. Property `Person > relationships`

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `object`                                      |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Defined in**            | #/definitions/person/properties/relationships |

**Description:** Relationships between this person and others

| Property                           | Pattern | Type   | Deprecated | Definition              | Title/Description |
| ---------------------------------- | ------- | ------ | ---------- | ----------------------- | ----------------- |
| - [mother](#relationships_mother ) | No      | object | No         | In #/definitions/person | A human being     |

### <a name="relationships_mother"></a>1.1. Property `Person > relationships > mother`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/definitions/person |

**Description:** A human being

| Property                                                | Pattern | Type   | Deprecated | Definition | Title/Description                            |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------------- |
| - [relationships](#relationships_mother_relationships ) | No      | object | No         | -          | Relationships between this person and others |

#### <a name="relationships_mother_relationships"></a>1.1.1. Property `Person > relationships > mother > relationships`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Relationships between this person and others

| Property                                                | Pattern | Type   | Deprecated | Definition                               | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------------------------------------- | ----------------- |
| - [mother](#relationships_mother_relationships_mother ) | No      | object | No         | Same as [mother](#relationships_mother ) | A human being     |

##### <a name="relationships_mother_relationships_mother"></a>1.1.1.1. Property `Person > relationships > mother > relationships > mother`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Same definition as**    | [mother](#relationships_mother) |

**Description:** A human being

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
