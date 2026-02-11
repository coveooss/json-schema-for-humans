# Schema Docs

- [1. Property `root > storage`](#storage)
  - [1.1. Property `root > storage > oneOf > diskDevice`](#storage_oneOf_i0)
  - [1.2. Property `root > storage > oneOf > diskUUID`](#storage_oneOf_i1)
  - [1.3. Property `root > storage > oneOf > nfs`](#storage_oneOf_i2)
  - [1.4. Property `root > storage > oneOf > tmpfs`](#storage_oneOf_i3)

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

**Description:** JSON Schema for an fstab entry

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
<li><a href="#">storage</a></li>
</ul></td>
    <td>No</td>
    <td>Combination</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

## <a name="storage"></a>1. Property `root > storage`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>combining</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>Yes</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

<table>
  <tr>
    <th>One of(Option)</th>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i0">diskDevice</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i1">diskUUID</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i2">nfs</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i3">tmpfs</a></td>
  </tr>
</table>

### <a name="storage_oneOf_i0"></a>1.1. Property `root > storage > oneOf > diskDevice`

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
    <td><h1>/definitions/diskDevice</h1></td>
  </tr>
</table>

### <a name="storage_oneOf_i1"></a>1.2. Property `root > storage > oneOf > diskUUID`

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
    <td><h1>/definitions/diskUUID</h1></td>
  </tr>
</table>

### <a name="storage_oneOf_i2"></a>1.3. Property `root > storage > oneOf > nfs`

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
    <td><h1>/definitions/nfs</h1></td>
  </tr>
</table>

### <a name="storage_oneOf_i3"></a>1.4. Property `root > storage > oneOf > tmpfs`

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
    <td><h1>/definitions/tmpfs</h1></td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
