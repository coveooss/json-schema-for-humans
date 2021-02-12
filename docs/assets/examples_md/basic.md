# Person

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`](#firstName)
- [2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`](#lastName)
- [3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > age`](#age)
- [4. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > driverLicenseId`](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [firstName](#firstName)|No|string|No|The person's first name.|
|-  [lastName](#lastName)|No|string|No|The person's last name.|
|-  [age](#age)|No|integer|No|Age in years which must be equal to or greater than zero.|
|-  [driverLicenseId](#driverLicenseId)|No|object|No|-|
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

## <a name="age"></a>3. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > age`

| Type | `integer` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |

## <a name="driverLicenseId"></a>4. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > driverLicenseId`

| Type | `combining` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| All of(Requirement) | 
| ---- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |
### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

| Type | `null` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:56:20 +0100