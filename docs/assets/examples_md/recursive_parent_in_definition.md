

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships)|No|object|No|No| No|Relationships between this person and others|

##  <a name="relationships"></a>1.  Property `Person > relationships`

**Description**:  Relationships between this person and others

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother)|No|object|No|No| No|A human being|

###  <a name="relationships_mother"></a>1.1.  Property `Person > relationships > mother`

**Description**:  A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships_mother_relationships)|No|object|No|No| No|Relationships between this person and others|

####  <a name="relationships_mother_relationships"></a>1.1.1.  Property `Person > relationships > mother > relationships`

**Description**:  Relationships between this person and others

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother_relationships_mother)|No|object|No|No| No|A human being|

#####  <a name="relationships_mother_relationships_mother"></a>1.1.1.1.  Property `Person > relationships > mother > relationships > mother`

**Description**:  A human being

    Same definition as [mother](#relationships_mother)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 00:44:55 +0100