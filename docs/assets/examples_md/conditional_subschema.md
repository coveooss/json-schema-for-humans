# Schema Docs

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_if"):**
  root
 >   if

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|country|No|const|No|No| No||

**[Then](#tab-pane_then):**
  root
 >   then

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#then_postal_code)|No|object|No|No| No||

  ## <a name="then_postal_code"></a>Property `postal_code`

      root
 >   then
 >   postal_code

Type: `object`

                Must match regular expression: `[0-9]{5}(-[0-9]{4})?` [Test](https://regex101.com/?regex=[0-9]{5}(-[0-9]{4})?)

**[Else](#tab-pane_else):**
  root
 >   else

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#else_postal_code)|No|object|No|No| No||

  ## <a name="else_postal_code"></a>Property `postal_code`

      root
 >   else
 >   postal_code

Type: `object`

                Must match regular expression: `[A-Z][0-9][A-Z] [0-9][A-Z][0-9]` [Test](https://regex101.com/?regex=[A-Z][0-9][A-Z] [0-9][A-Z][0-9])

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|street_address|No|string|No|No| No||
|country|No|enum (of string)|No|No| No||

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 20:34:35 +0100