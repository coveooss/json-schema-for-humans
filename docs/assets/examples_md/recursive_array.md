# Person
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|person|No|array|No|No| No|A list of people|

## <a name="person"></a> 1. Property `Person > person`

**Description**:  A list of people

    Type: `array`

**Description:** A list of people

#### Each item of this array must be
Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|children|No|array|No|No| No|The children they had|

### <a name="person_items_children"></a> 1.1. Property `Person > person > items > children`

**Description**:  The children they had

    Type: `array`

**Description:** The children they had

#### Each item of this array must be
Type: `object`

**Description:** A human being
        Same definition as [person](#person_items)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:49 +0100