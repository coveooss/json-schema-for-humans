# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Pattern Property `Person > paperSize`](#pattern1)
  - [3.1. Property `Person > paperSize > rating`](#pattern1_rating)
  - [3.2. Property `Person > paperSize > review`](#pattern1_review)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|Combination|No|No| No|The person's first name.|
| [lastName](#lastName)|No|Combination|No|No| No|The person's last name.|
| [$[a-c][0-9]^](#pattern1)|Yes|Combination|No|No| No|Review of a paper size.|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="firstName"></a>1. Property `Person > firstName`

Type: `string`

**Description:** <p>The person's first name.</p>

## <a name="lastName"></a>2. Property `Person > lastName`

Type: `string`

**Description:** <p>The person's last name.</p>

## <a name="pattern1"></a>3. Pattern Property `Person > paperSize`> All property whose name matches the following regular expression must respect the following conditions
  Property name regular expression: 
[`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

> All property whose name matches the following regular expression must respect the following conditions
  Property name regular expression: 
[`$[a-c][0-9]^`](https://regex101.com/?regex=$[a-c][0-9]^

Type: `object`

**Description:** <p>Review of a paper size.</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [rating](#pattern1_rating)|No|Combination|Yes|No| No|Numerical rating for paper size.|
| [review](#pattern1_review)|No|Combination|Yes|No| No|Narrative review of the paper size.|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="pattern1_rating"></a>3.1. Property `Person > paperSize > rating`

Type: `integer`

**Description:** <p>Numerical rating for paper size.</p>

### <a name="pattern1_review"></a>3.2. Property `Person > paperSize > review`

Type: `string`

**Description:** <p>Narrative review of the paper size.</p>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:35 +0100