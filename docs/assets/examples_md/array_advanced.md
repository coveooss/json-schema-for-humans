# Schema Docs

Type: `object`

**Description:** A little food fun

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|fruits|No|array of string|No|No| No|5 to 8 fruits that you like|
|vegetables|No|array|No|No| No||

## <a name="fruits"></a> 1. Property `fruits`

**Description**:  5 to 8 fruits that you like

      root
 >   fruits

Type: `array of string`

**Description:** 5 to 8 fruits that you like

    Must contain a minimum of `5` items

    Must contain a maximum of `8` items

    All items must be unique

#### Each item of this array must be
  root
 >   fruits
 >   items

Type: `string`

## <a name="vegetables"></a> 2. Property `vegetables`

      root
 >   vegetables

Type: `array`

#### Each item of this array must be
  root
 >   vegetables
 >   items

Type: `object`

#### At least one of the items must be
  root
 >   vegetables
 >   contains

Type: `const`

                Specific value: `"eggplant"`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:22 +0100