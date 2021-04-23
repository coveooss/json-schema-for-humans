# Person

**Title:** Person

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary>

## <a name="firstName"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `firstName`  

</summary>
<blockquote>

**Title:** Person

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary>

## <a name="lastName"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `lastName`  

</summary>
<blockquote>

**Title:** Person

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary>

## <a name="age"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `age`  

</summary>
<blockquote>

**Title:** Person

| Type                      | `integer`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
|              |        |

</blockquote>
</details>

<details>
<summary>

## <a name="driverLicenseId"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `driverLicenseId`  

</summary>
<blockquote>

| Type                      | `combining`                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<blockquote>

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |
|                                                |

### <a name="driverLicenseId_allOf_i0"></a>Property `no driver licence`

**Title:** no driver licence

| Type                      | `null`                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

### <a name="driverLicenseId_allOf_i1"></a>Property `driver licence id`

**Title:** driver licence id

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date