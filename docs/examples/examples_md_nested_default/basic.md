# Person

- [1. [Optional] Property Person > firstName](#firstName-4e616d65)
- [2. [Optional] Property Person > lastName](#lastName-4e616d65)
- [3. [Optional] Property Person > age](#age-616765)
- [4. [Optional] Property Person > driverLicenseId](#driverLicenseId-73654964)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0-665f6930)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1-665f6931)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="firstName-4e616d65"></a>1. [Optional] Property Person > firstName</strong>  

</summary>
<blockquote>

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary><strong> <a name="lastName-4e616d65"></a>2. [Optional] Property Person > lastName</strong>  

</summary>
<blockquote>

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary><strong> <a name="age-616765"></a>3. [Optional] Property Person > age</strong>  

</summary>
<blockquote>

**Title:** Person

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary><strong> <a name="driverLicenseId-73654964"></a>4. [Optional] Property Person > driverLicenseId</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<blockquote>

| All of(Requirement)                                     |
| ------------------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0-665f6930) |
| [driver licence id](#driverLicenseId_allOf_i1-665f6931) |

<blockquote>

### <a name="driverLicenseId_allOf_i0-665f6930"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

</blockquote>
<blockquote>

### <a name="driverLicenseId_allOf_i1-665f6931"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)