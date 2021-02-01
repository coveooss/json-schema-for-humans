# Schema Docs
Type: `object`

**Description:** A little food fun

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|fruits|No|array of string|No|No| No|5 to 8 fruits that you like|
|vegetables|No|array|No|No| No||

## <a name="fruits"></a> 1. Property `root > fruits`

**Description**:  5 to 8 fruits that you like

    Type: `array of string`

**Description:** 5 to 8 fruits that you like

    Must contain a minimum of `5` items

    Must contain a maximum of `8` items

    All items must be unique

#### Each item of this array must be
Type: `string`

## <a name="vegetables"></a> 2. Property `root > vegetables`

    Type: `array`

#### Each item of this array must be
Type: `object`

#### At least one of the items must be
Type: `const`

                Specific value: `"eggplant"`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:50 +0100