# Test

- [1. Property `Test > aProperty`](#aProperty)
- [2. Property `Test > aDictPropertyARequired`](#aDictPropertyARequired)
  - [2.1. Property `Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a)
  - [2.2. Property `Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b)

**Title:** Test

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">aProperty</a></li>
</ul></td>
    <td>No</td>
    <td>enum (of string)</td>
    <td>No</td>
    <td>In #/definitions/aProperty</td>
    <td>Title from definition</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">aDictPropertyARequired</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/aDictProperty</td>
    <td>-</td>
  </tr>
</table>

## <a name="aProperty"></a>1. Property `Test > aProperty`

**Title:** Title from definition

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>"Default from property"</code></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/aProperty</h1></td>
  </tr>
</table>

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. Property `Test > aDictPropertyARequired`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>{"a": "a", "b": "b"}</code></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/aDictProperty</h1></td>
  </tr>
</table>

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">a</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">b</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="aDictPropertyARequired_a"></a>2.1. Property `Test > aDictPropertyARequired > a`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
</table>

### <a name="aDictPropertyARequired_b"></a>2.2. Property `Test > aDictPropertyARequired > b`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
