# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Pattern Property `Person > paperSize`](#pattern1)
  - [3.1. Property `Person > paperSize > rating`](#pattern1_rating)
  - [3.2. Property `Person > paperSize > review`](#pattern1_review)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [firstName](#firstName )   | No      | string | No         | -          | Person            |
| - [lastName](#lastName )     | No      | string | No         | -          | Person            |
| - [$[a-c][0-9]^](#pattern1 ) | Yes     | object | No         | -          | paperSize         |

## <a name="firstName"></a>1. Property `Person > firstName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's last name.

## <a name="pattern1"></a>3. Pattern Property `Person > paperSize`
> All properties whose name matches the regular expression
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

**Title:** paperSize

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Review of a paper size.

| Property                      | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [rating](#pattern1_rating ) | No      | integer | No         | -          | Rating            |
| + [review](#pattern1_review ) | No      | string  | No         | -          | Review            |

### <a name="pattern1_rating"></a>3.1. Property `Person > paperSize > rating`

**Title:** Rating

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Numerical rating for paper size.

### <a name="pattern1_review"></a>3.2. Property `Person > paperSize > review`

**Title:** Review

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
