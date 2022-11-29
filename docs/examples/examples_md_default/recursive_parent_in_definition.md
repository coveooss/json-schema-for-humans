# Person

- [1. Property `Person > relationships`](#relationships-68697073)
  - [1.1. Property `Person > relationships > mother`](#relationships_mother-74686572)
    - [1.1.1. Property `Person > relationships > mother > relationships`](#relationships_mother_relationships-68697073)
      - [1.1.1.1. Property `Person > relationships > mother > relationships > mother`](#relationships_mother_relationships_mother-74686572)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                    | Pattern | Type   | Deprecated | Definition                                       | Title/Description                            |
| ------------------------------------------- | ------- | ------ | ---------- | ------------------------------------------------ | -------------------------------------------- |
| - [relationships](#relationships-68697073 ) | No      | object | No         | In #/definitions/person/properties/relationships | Relationships between this person and others |

## <a name="relationships-68697073"></a>1. Property `Person > relationships`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person/properties/relationships                             |

**Description:** Relationships between this person and others

| Property                                    | Pattern | Type   | Deprecated | Definition              | Title/Description |
| ------------------------------------------- | ------- | ------ | ---------- | ----------------------- | ----------------- |
| - [mother](#relationships_mother-74686572 ) | No      | object | No         | In #/definitions/person | A human being     |

### <a name="relationships_mother-74686572"></a>1.1. Property `Person > relationships > mother`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/person                                                      |

**Description:** A human being

| Property                                                         | Pattern | Type   | Deprecated | Definition | Title/Description                            |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------------- |
| - [relationships](#relationships_mother_relationships-68697073 ) | No      | object | No         | -          | Relationships between this person and others |

#### <a name="relationships_mother_relationships-68697073"></a>1.1.1. Property `Person > relationships > mother > relationships`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Relationships between this person and others

| Property                                                         | Pattern | Type   | Deprecated | Definition                                        | Title/Description |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------------------------- | ----------------- |
| - [mother](#relationships_mother_relationships_mother-74686572 ) | No      | object | No         | Same as [mother](#relationships_mother-74686572 ) | A human being     |

##### <a name="relationships_mother_relationships_mother-74686572"></a>1.1.1.1. Property `Person > relationships > mother > relationships > mother`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [mother](#relationships_mother)                                           |

**Description:** A human being

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
