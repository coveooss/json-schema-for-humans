# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|firstName|No|string|No|No| No|The person's first name.|
|lastName|No|string|No|No| No|The person's last name.|
|$[a-c][0-9]^|Yes|object|No|No| No|Review of a paper size.|

## <a name="firstName"></a> 1. Property `firstName`

**Description**:  The person's first name.

      Person
 >   firstName

Type: `string`

**Description:** The person's first name.

## <a name="lastName"></a> 2. Property `lastName`

**Description**:  The person's last name.

      Person
 >   lastName

Type: `string`

**Description:** The person's last name.

## <a name="pattern1"></a> 3. Pattern Property `$[a-c][0-9]^`
  > All property whose name matches the following regular expression must respect the following conditions
    Property name regular expression: 
  [`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

**Description**:  Review of a paper size.
  > All property whose name matches the following regular expression must respect the following conditions
    Property name regular expression: 
  [`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

      Person
 >   paperSize

Type: `object`

**Description:** Review of a paper size.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|rating|No|integer|Yes|No| No|Numerical rating for paper size.|
|review|No|string|Yes|No| No|Narrative review of the paper size.|

### <a name="pattern1_rating"></a> 3.1. Property `rating`

**Description**:  Numerical rating for paper size.

      Person
 >   paperSize
 >   rating

Type: `integer`

**Description:** Numerical rating for paper size.

### <a name="pattern1_review"></a> 3.2. Property `review`

**Description**:  Narrative review of the paper size.

      Person
 >   paperSize
 >   review

Type: `string`

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:21 +0100