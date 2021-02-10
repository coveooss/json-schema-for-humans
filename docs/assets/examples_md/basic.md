# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|The person's first name.|
| [lastName](#lastName)|No|string|No|No| No|The person's last name.|
| [age](#age)|No|integer|No|No| No|Age in years which must be equal to or greater than zero.|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="firstName"></a>1. Property `Person > firstName`

Type: `string`

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

Type: `string`

**Description:** The person's last name.

## <a name="age"></a>3. Property `Person > age`

Type: `integer`

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 00:42:30 +0100