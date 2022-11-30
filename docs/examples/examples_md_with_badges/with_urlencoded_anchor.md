# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`](#signingTimeInfo)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`](#signingTimeInfo_signingTime)
  - [1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`](#signingTimeInfo_signingTimeBounds_upperBound)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                               | Pattern | Type   | Deprecated | Definition                                | Title/Description |
| -------------------------------------- | ------- | ------ | ---------- | ----------------------------------------- | ----------------- |
| - [signingTimeInfo](#signingTimeInfo ) | No      | object | No         | In #/definitions/dss2-SigningTimeInfoType | -                 |

## <a name="signingTimeInfo"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType                                                                                            |

| Property                                                   | Pattern | Type    | Deprecated | Definition                                                        | Title/Description |
| ---------------------------------------------------------- | ------- | ------- | ---------- | ----------------------------------------------------------------- | ----------------- |
| + [signingTime](#signingTimeInfo_signingTime )             | No      | integer | No         | -                                                                 | -                 |
| - [signingTimeBounds](#signingTimeInfo_signingTimeBounds ) | No      | object  | No         | In #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries | -                 |

### <a name="signingTimeInfo_signingTime"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

### <a name="signingTimeInfo_signingTimeBounds"></a>1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries                                                                    |

| Property                                                       | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound ) | No      | integer | No         | -          | -                 |
| - [upperBound](#signingTimeInfo_signingTimeBounds_upperBound ) | No      | integer | No         | -          | -                 |

#### <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

#### <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`

|            |                |
| ---------- | -------------- |
| **Type**   | `integer`      |
| **Format** | `utc-millisec` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
