# Schema Docs

Type: `object`

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No||

## <a name="storage"></a>Property `storage`

      root
 >   storage

                [[]
<a id="storage_oneOf" href="#storage_oneOf">
    <h2 class="handle ml-2 mt-2">
      <label>One of</label>
    </h2>
</a>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_oneOf_i0" href="#storage_oneOf_i0">diskDevice</a></h3>
        <div class="card-body">
              root
 >   storage
 >   oneOf
 >   diskDevice

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_oneOf_i1" href="#storage_oneOf_i1">diskUUID</a></h3>
        <div class="card-body">
              root
 >   storage
 >   oneOf
 >   diskUUID

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_oneOf_i2" href="#storage_oneOf_i2">nfs</a></h3>
        <div class="card-body">
              root
 >   storage
 >   oneOf
 >   nfs

Type: `object`

        </div>
    </div>
    <div class="card">
        <h3 class="ml-2 mt-2"><a id="storage_oneOf_i3" href="#storage_oneOf_i3">tmpfs</a></h3>
        <div class="card-body">
              root
 >   storage
 >   oneOf
 >   tmpfs

Type: `object`

        </div>
    </div>
](storage_oneOf)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 13:13:15 +0100