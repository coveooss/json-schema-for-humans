# Person

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`](#firstName)
- [2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`](#lastName)
- [3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)Pattern Property `Person > paperSize`](#pattern1)
  - [3.1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > rating`](#pattern1_rating)
  - [3.2. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > review`](#pattern1_review)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [firstName](#firstName)|No|string|No|The person's first name.|
|-  [lastName](#lastName)|No|string|No|The person's last name.|
|-  [$[a-c][0-9]^](#pattern1)|Yes|object|No|Review of a paper size.|
|  |  |  |  |  |

## <a name="firstName"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** The person's first name.

## <a name="lastName"></a>2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** The person's last name.

## <a name="pattern1"></a>3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)Pattern Property `Person > paperSize`
> All property whose name matches the regular expression 
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Review of a paper size.

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|+  [rating](#pattern1_rating)|No|integer|No|Numerical rating for paper size.|
|+  [review](#pattern1_review)|No|string|No|Narrative review of the paper size.|
|  |  |  |  |  |

### <a name="pattern1_rating"></a>3.1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > rating`

| Type | `integer` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Numerical rating for paper size.

### <a name="pattern1_review"></a>3.2. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Person > paperSize > review`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:34:12 +0100