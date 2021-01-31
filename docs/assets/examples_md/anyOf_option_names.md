# Schema Docs

Type: `object`

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No||

## <a name="storage"></a> 1. Property `storage`

      root
 >   storage

                [[]
<a id="storage_anyOf" href="#storage_anyOf">
    <h2 class="handle ml-2 mt-2">
      <label>Any of</label>
    </h2>
</a>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_anyOf_i0" href="#storage_anyOf_i0">diskDevice</a></h3>
        <div class="card-body">
              root
 >   storage
 >   anyOf
 >   diskDevice

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_anyOf_i1" href="#storage_anyOf_i1">diskUUID</a></h3>
        <div class="card-body">
              root
 >   storage
 >   anyOf
 >   diskUUID

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_anyOf_i2" href="#storage_anyOf_i2">Option 3</a></h3>
        <div class="card-body">
              root
 >   storage
 >   anyOf
 >   item 2

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_anyOf_i3" href="#storage_anyOf_i3">tmpfs</a></h3>
        <div class="card-body">
              root
 >   storage
 >   anyOf
 >   tmpfs

Type: `object`

        </div>
    </div>
](storage_anyOf)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 23:30:22 +0100