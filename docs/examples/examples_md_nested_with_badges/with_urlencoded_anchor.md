# Schema Docs

- [1. [Optional] Propertyroot > signingTimeInfo](#signingTimeInfo)
  - [1.1. [Required] Propertyroot > signingTimeInfo > signingTime](#signingTimeInfo_signingTime)
  - [1.2. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds > lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds > upperBound](#signingTimeInfo_signingTimeBounds_upperBound)

|          |          |
| -------- | -------- |
| **Type** | `object` |

<details>
<summary>
<strong> <a name="signingTimeInfo"></a>1. [Optional] Propertyroot > signingTimeInfo</strong>  

</summary>
<blockquote>

|                |                                        |
| -------------- | -------------------------------------- |
| **Type**       | `object`                               |
| **Defined in** | #/definitions/dss2-SigningTimeInfoType |

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTime"></a>1.1. [Required] Propertyroot > signingTimeInfo > signingTime</strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds"></a>1.2. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds</strong>  

</summary>
<blockquote>

|                |                                                                |
| -------------- | -------------------------------------------------------------- |
| **Type**       | `object`                                                       |
| **Defined in** | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries |

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds > lowerBound</strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. [Optional] Propertyroot > signingTimeInfo > signingTimeBounds > upperBound</strong>  

</summary>
<blockquote>

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)