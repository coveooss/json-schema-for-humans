# Schema Docs

Type: `object`

**Description:** Testing $ref of a remote $ref

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [described](#described)|No|object|No|No| No||

## <a name="described"></a> 1. Property `described`

      root
 >   described

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|name|No|string|No|No| No|a filled string|
|alignment|No|string|No|No| No|a filled string|
`No Additional Properties`

### <a name="described_name"></a> 1.1. Property `name`

**Description**:  a filled string

      root
 >   described
 >   name

Type: `string`

**Description:** a filled string

        Must be at least `1` characters long

### <a name="described_alignment"></a> 1.2. Property `alignment`

**Description**:  a filled string

      root
 >   described
 >   alignment

Type: `string`

**Description:** a filled string
        Same definition as [name](#described_name)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:23 +0100