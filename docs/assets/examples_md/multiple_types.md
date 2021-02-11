# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > anything`](#anything)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No| No|The person's first name.|
| [lastName](#lastName)|No|string or null|No| No|The person's last name.|
| [age](#age)|No|integer or number|No| No|Age in years which must be equal to or greater than zero.|
| [anything](#anything)|No|integer, string, number or null|No| No|Ay other info you like|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="firstName"></a>1. Property `Person > firstName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string or null`

**Description:** The person's last name.

## <a name="age"></a>3. Property `Person > age`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `integer or number`

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |

## <a name="anything"></a>4. Property `Person > anything`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `integer, string, number or null`

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:06 +0100