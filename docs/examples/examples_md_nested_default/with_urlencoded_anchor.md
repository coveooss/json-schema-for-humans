# Schema Docs

- [1. [Optional] Property root > signingTimeInfo](#signingTimeInfo-496e666f)
  - [1.1. [Required] Property root > signingTimeInfo > signingTime](#signingTimeInfo_signingTime-54696d65)
  - [1.2. [Optional] Property root > signingTimeInfo > signingTimeBounds](#signingTimeInfo_signingTimeBounds-756e6473)
    - [1.2.1. [Optional] Property root > signingTimeInfo > signingTimeBounds > lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound-6f756e64)
    - [1.2.2. [Optional] Property root > signingTimeInfo > signingTimeBounds > upperBound](#signingTimeInfo_signingTimeBounds_upperBound-6f756e64)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="signingTimeInfo-496e666f"></a>1. [Optional] Property root > signingTimeInfo</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType                                    |

<details>
<summary><strong> <a name="signingTimeInfo_signingTime-54696d65"></a>1.1. [Required] Property root > signingTimeInfo > signingTime</strong>  

</summary>
<blockquote>

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | Yes            |
| **Format**   | `utc-millisec` |

</blockquote>
</details>

<details>
<summary><strong> <a name="signingTimeInfo_signingTimeBounds-756e6473"></a>1.2. [Optional] Property root > signingTimeInfo > signingTimeBounds</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries            |

<details>
<summary><strong> <a name="signingTimeInfo_signingTimeBounds_lowerBound-6f756e64"></a>1.2.1. [Optional] Property root > signingTimeInfo > signingTimeBounds > lowerBound</strong>  

</summary>
<blockquote>

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | No             |
| **Format**   | `utc-millisec` |

</blockquote>
</details>

<details>
<summary><strong> <a name="signingTimeInfo_signingTimeBounds_upperBound-6f756e64"></a>1.2.2. [Optional] Property root > signingTimeInfo > signingTimeBounds > upperBound</strong>  

</summary>
<blockquote>

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | No             |
| **Format**   | `utc-millisec` |

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)