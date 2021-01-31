# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|person|No|array|No|No| No|A list of people|

## <a name="person"></a> 1. Property `person`

**Description**:  A list of people

      Person
 >   person

Type: `array`

**Description:** A list of people

#### Each item of this array must be
  Person
 >   person
 >   person

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|children|No|array|No|No| No|The children they had|

### <a name="person_items_children"></a> 1.1. Property `children`

**Description**:  The children they had

      Person
 >   person
 >   items
 >   children

Type: `array`

**Description:** The children they had

#### Each item of this array must be
  Person
 >   person
 >   items
 >   children
 >   person

Type: `object`

**Description:** A human being
        Same definition as [person](#person_items)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:21 +0100