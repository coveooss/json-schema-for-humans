# Schema Docs
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [outer](#outer)|No|object|Yes|No| No|We should see this|
| [outer2](#outer2)|No|object|No|No| No|We should see this too|
`No Additional Properties`

## <a name="outer"></a> 1. Property `root > outer`

**Description**:  We should see this

    Type: `object`

**Description:** We should see this

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|inner|No|string|Yes|No| No|inner description|
`No Additional Properties`

### <a name="outer_inner"></a> 1.1. Property `root > outer > inner`

**Description**:  inner description

    Type: `string`

**Description:** inner description

## <a name="outer2"></a> 2. Property `root > outer2`

**Description**:  We should see this too

    Type: `object`

**Description:** We should see this too
        Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:48 +0100