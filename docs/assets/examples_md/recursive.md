# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|A human being|

## <a name="person"></a> 1. Property `person`

**Description**:  A human being

      Person
 >   person

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|children|No|array|No|No| No|The children they had|

### <a name="person_children"></a> 1.1. Property `children`

**Description**:  The children they had

      Person
 >   person
 >   children

Type: `array`

**Description:** The children they had

#### Each item of this array must be
  Person
 >   person
 >   children
 >   person

Type: `object`

**Description:** A human being
        Same definition as [person](#person)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:22 +0100