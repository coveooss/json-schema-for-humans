# Schema Docs

- [1. Property `root > signingTimeInfo`](#signingTimeInfo)
  - [1.1. Property `root > signingTimeInfo > signingTime`](#signingTimeInfo_signingTime)
  - [1.2. Property `root > signingTimeInfo > signingTimeBounds`](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. Property `root > signingTimeInfo > signingTimeBounds > lowerBound`](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. Property `root > signingTimeInfo > signingTimeBounds > upperBound`](#signingTimeInfo_signingTimeBounds_upperBound)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                               | Pattern | Type   | Deprecated | Definition                                | Title/Description |
| -------------------------------------- | ------- | ------ | ---------- | ----------------------------------------- | ----------------- |
| - [signingTimeInfo](#signingTimeInfo ) | No      | object | No         | In #/definitions/dss2-SigningTimeInfoType | -                 |

## <a name="signingTimeInfo"></a>1. Property `root > signingTimeInfo`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType                                    |

| Property                                                   | Pattern | Type    | Deprecated | Definition                                                        | Title/Description |
| ---------------------------------------------------------- | ------- | ------- | ---------- | ----------------------------------------------------------------- | ----------------- |
| + [signingTime](#signingTimeInfo_signingTime )             | No      | integer | No         | -                                                                 | -                 |
| - [signingTimeBounds](#signingTimeInfo_signingTimeBounds ) | No      | object  | No         | In #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries | -                 |

### <a name="signingTimeInfo_signingTime"></a>1.1. Property `root > signingTimeInfo > signingTime`

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | Yes            |
| **Format**   | `utc-millisec` |

### <a name="signingTimeInfo_signingTimeBounds"></a>1.2. Property `root > signingTimeInfo > signingTimeBounds`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries            |

| Property                                                       | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound ) | No      | integer | No         | -          | -                 |
| - [upperBound](#signingTimeInfo_signingTimeBounds_upperBound ) | No      | integer | No         | -          | -                 |

#### <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. Property `root > signingTimeInfo > signingTimeBounds > lowerBound`

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | No             |
| **Format**   | `utc-millisec` |

#### <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. Property `root > signingTimeInfo > signingTimeBounds > upperBound`

|              |                |
| ------------ | -------------- |
| **Type**     | `integer`      |
| **Required** | No             |
| **Format**   | `utc-millisec` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
