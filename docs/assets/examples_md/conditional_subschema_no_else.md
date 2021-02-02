

# Schema Docs

            [[]
<a id="allOf" href="#allOf">
    <h2 class="handle ml-2 mt-2">
      <label>All of</label>
    </h2>
</a>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="allOf_i0" href="#allOf_i0">Requirement 1</a></h3>
        <div class="card-body">

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i0_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i0_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i0_if_country"></a>1.  Property `root > allOf > item 0 > if > country`

Type: `const`

            Specific value: `"United States of America"`

**[Then](#tab-pane_allOf_i0_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i0_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i0_then_postal_code"></a>1.  Property `root > allOf > item 0 > then > postal_code`

Type: `object`

            Must match regular expression: `[0-9]{5}(-[0-9]{4})?` [Test](https://regex101.com/?regex=[0-9]{5}(-[0-9]{4})?)

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="allOf_i1" href="#allOf_i1">Requirement 2</a></h3>
        <div class="card-body">

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i1_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i1_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i1_if_country"></a>1.  Property `root > allOf > item 1 > if > country`

Type: `const`

            Specific value: `"Canada"`

**[Then](#tab-pane_allOf_i1_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i1_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i1_then_postal_code"></a>1.  Property `root > allOf > item 1 > then > postal_code`

Type: `object`

            Must match regular expression: `[A-Z][0-9][A-Z] [0-9][A-Z][0-9]` [Test](https://regex101.com/?regex=[A-Z][0-9][A-Z] [0-9][A-Z][0-9])

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="allOf_i2" href="#allOf_i2">Requirement 3</a></h3>
        <div class="card-body">

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i2_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i2_if_country)|No|const|No|No| No|-|

##  <a name="allOf_i2_if_country"></a>1.  Property `root > allOf > item 2 > if > country`

Type: `const`

            Specific value: `"Netherlands"`

**[Then](#tab-pane_allOf_i2_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i2_then_postal_code)|No|object|No|No| No|-|

##  <a name="allOf_i2_then_postal_code"></a>1.  Property `root > allOf > item 2 > then > postal_code`

Type: `object`

            Must match regular expression: `[0-9]{4} [A-Z]{2}` [Test](https://regex101.com/?regex=[0-9]{4} [A-Z]{2})

        </div>
    </div>
](allOf)

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#street_address)|No|string|No|No| No|-|
| [country](#country)|No|enum (of string)|No|No| No|-|

##  <a name="street_address"></a>1.  Property `root > street_address`

Type: `string`

##  <a name="country"></a>2.  Property `root > country`

Type: `enum (of string)`

            Must be one of:
                * "United States of America"
                * "Canada"
                * "Netherlands"

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 21:26:33 +0100