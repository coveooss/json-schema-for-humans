# Person

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`](#firstName)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`](#lastName)
- [3. ![badge](https://img.shields.io/badge/Optional-yellow)Pattern Property `Person > paperSize`](#pattern1)
  - [3.1. ![badge](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > rating`](#pattern1_rating)
  - [3.2. ![badge](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > review`](#pattern1_review)

**Title:** Person

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [firstName](#firstName )   | No      | string | No         | -          | Person            |
| - [lastName](#lastName )     | No      | string | No         | -          | Person            |
| - [$[a-c][0-9]^](#pattern1 ) | Yes     | object | No         | -          | paperSize         |
|                              |         |        |            |            |                   |

## <a name="firstName"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`

**Title:** Person

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The person's first name.

## <a name="lastName"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`

**Title:** Person

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The person's last name.

## <a name="pattern1"></a>3. ![badge](https://img.shields.io/badge/Optional-yellow)Pattern Property `Person > paperSize`
> All property whose name matches the regular expression 
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

**Title:** paperSize

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Review of a paper size.

| Property                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [rating](#pattern1_rating ) | No      | integer | No         | -          | Rating            |
| + [review](#pattern1_review ) | No      | string  | No         | -          | Review            |
|                               |         |         |            |            |                   |

### <a name="pattern1_rating"></a>3.1. ![badge](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > rating`

**Title:** Rating

| Type                      | `integer`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Numerical rating for paper size.

### <a name="pattern1_review"></a>3.2. ![badge](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > review`

**Title:** Review

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date