# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Pattern Property `Person > paperSize`](#pattern1)
  - [3.1. Property `Person > paperSize > rating`](#pattern1_rating)
  - [3.2. Property `Person > paperSize > review`](#pattern1_review)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [firstName](#firstName)|No|string|No| No|The person's first name.|
|-  [lastName](#lastName)|No|string|No| No|The person's last name.|
|-  [$[a-c][0-9]^](#pattern1)|Yes|object|No| No|Review of a paper size.|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="firstName"></a>1. Property `Person > firstName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** The person's last name.

## <a name="pattern1"></a>3. Pattern Property `Person > paperSize`
> All property whose name matches the regular expression 
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** Review of a paper size.

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [rating](#pattern1_rating)|No|integer|No| No|Numerical rating for paper size.|
|+  [review](#pattern1_review)|No|string|No| No|Narrative review of the paper size.|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="pattern1_rating"></a>3.1. Property `Person > paperSize > rating`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `integer`

**Description:** Numerical rating for paper size.

### <a name="pattern1_review"></a>3.2. Property `Person > paperSize > review`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:29 +0100