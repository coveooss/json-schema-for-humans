# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`](#signingTimeInfo-496e666f)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`](#signingTimeInfo_signingTime-54696d65)
  - [1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`](#signingTimeInfo_signingTimeBounds-756e6473)
    - [1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`](#signingTimeInfo_signingTimeBounds_lowerBound-6f756e64)
    - [1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`](#signingTimeInfo_signingTimeBounds_upperBound-6f756e64)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                        | Pattern | Type   | Deprecated | Definition                                | Title/Description |
| ----------------------------------------------- | ------- | ------ | ---------- | ----------------------------------------- | ----------------- |
| - [signingTimeInfo](#signingTimeInfo-496e666f ) | No      | object | No         | In #/definitions/dss2-SigningTimeInfoType | -                 |

## <a name="signingTimeInfo-496e666f"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType                                                                                            |

| Property                                                            | Pattern | Type    | Deprecated | Definition                                                        | Title/Description |
| ------------------------------------------------------------------- | ------- | ------- | ---------- | ----------------------------------------------------------------- | ----------------- |
| + [signingTime](#signingTimeInfo_signingTime-54696d65 )             | No      | integer | No         | -                                                                 | -                 |
| - [signingTimeBounds](#signingTimeInfo_signingTimeBounds-756e6473 ) | No      | object  | No         | In #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries | -                 |

### <a name="signingTimeInfo_signingTime-54696d65"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

### <a name="signingTimeInfo_signingTimeBounds-756e6473"></a>1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries                                                                    |

| Property                                                                | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound-6f756e64 ) | No      | integer | No         | -          | -                 |
| - [upperBound](#signingTimeInfo_signingTimeBounds_upperBound-6f756e64 ) | No      | integer | No         | -          | -                 |

#### <a name="signingTimeInfo_signingTimeBounds_lowerBound-6f756e64"></a>1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

#### <a name="signingTimeInfo_signingTimeBounds_upperBound-6f756e64"></a>1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
