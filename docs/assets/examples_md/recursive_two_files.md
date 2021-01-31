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
| [siblings](#person_siblings)|No|object|No|No| No|Person definition from second file. Not the same!|

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

**Description:** Person definition from second file. Not the same!
        Same definition as [siblings](#person_siblings)

### <a name="person_siblings"></a> 1.2. Property `siblings`

**Description**:  Person definition from second file. Not the same!

      Person
 >   person
 >   siblings

Type: `object`

**Description:** Person definition from second file. Not the same!

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:18 +0100