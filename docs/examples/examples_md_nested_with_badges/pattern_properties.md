# Person

- [1. [Optional] Property Person > firstName](#firstName)
- [2. [Optional] Property Person > lastName](#lastName)
- [3. [Optional]Pattern Property Person > paperSize](#pattern1)
  - [3.1. [Required] Property Person > paperSize > rating](#pattern1_rating)
  - [3.2. [Required] Property Person > paperSize > review](#pattern1_review)

**Title:** Person

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="firstName"></a>1. [Optional] Property Person > firstName</strong>  

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
<summary><strong> <a name="lastName"></a>2. [Optional] Property Person > lastName</strong>  

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
<summary><strong> <a name="pattern1"></a>3. [Optional]Pattern Property Person > paperSize</strong>  
> All property whose name matches the regular expression 
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

</summary>
<blockquote>

**Title:** paperSize

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Review of a paper size.

<details>
<summary><strong> <a name="pattern1_rating"></a>3.1. [Required] Property Person > paperSize > rating</strong>  

</summary>
<blockquote>

**Title:** Rating

| Type                      | `integer`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Numerical rating for paper size.

</blockquote>
</details>

<details>
<summary><strong> <a name="pattern1_review"></a>3.2. [Required] Property Person > paperSize > review</strong>  

</summary>
<blockquote>

**Title:** Review

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Narrative review of the paper size.

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date