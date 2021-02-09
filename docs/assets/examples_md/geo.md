# Longitude and Latitude Values

- [1. Property `Longitude and Latitude Values > latitude`](#latitude)
- [2. Property `Longitude and Latitude Values > longitude`](#longitude)

Type: `object`

**Description:** <p>A geographical coordinate.</p>

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [latitude](#latitude)|No|Combination|Yes|No| No|-|
| [longitude](#longitude)|No|Combination|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="latitude"></a>1. Property `Longitude and Latitude Values > latitude`

Type: `number`

|              | Restrictions |
| ------------ | ------------ |
| **Minimum** | &ge; -90 |
| **Maximum** | &le; 90 |

## <a name="longitude"></a>2. Property `Longitude and Latitude Values > longitude`

Type: `number`

|              | Restrictions |
| ------------ | ------------ |
| **Minimum** | &ge; -180 |
| **Maximum** | &le; 180 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:36 +0100