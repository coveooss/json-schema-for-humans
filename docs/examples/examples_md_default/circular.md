# Circular reference Schema

- [1. Property `Circular reference Schema > person`](#person)
  - [1.1. Property `Circular reference Schema > person > a1`](#person_a1)

**Title:** Circular reference Schema

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
<li><a href="#">person</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/a</td>
    <td>-</td>
  </tr>
</table>

## <a name="person"></a>1. Property `Circular reference Schema > person`

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
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/a</h1></td>
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
<li><a href="#">a1</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>In #/definitions/b</td>
    <td>Description from b</td>
  </tr>
</table>

### <a name="person_a1"></a>1.1. Property `Circular reference Schema > person > a1`

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
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>"Default from c"</code></td>
  </tr>
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/b</h1></td>
  </tr>
</table>

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
