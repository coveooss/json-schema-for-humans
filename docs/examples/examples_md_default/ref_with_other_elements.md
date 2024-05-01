# OF

- [1. Property `OF > uuid`](#uuid)
- [2. Property `OF > firstName`](#firstName)
- [3. Property `OF > lastName`](#lastName)

**Title:** OF

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                   | Pattern | Type   | Deprecated | Definition          | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------- | ----------------- |
| - [uuid](#uuid )           | No      | string | No         | In #/$defs/ofString | Unique Identifer  |
| - [firstName](#firstName ) | No      | string | No         | In #/$defs/ofString | first name        |
| - [lastName](#lastName )   | No      | string | No         | In #/$defs/ofString | last name         |

## <a name="uuid"></a>1. Property `OF > uuid`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** Unique Identifer

**Example:** 

```json
"29292929292929292929292"
```

**Example:** 

```json
"29292929292929292929292"
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 5   |
| **Max length** | 250 |

## <a name="firstName"></a>2. Property `OF > firstName`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** first name

**Example:** 

```json
"John"
```

**Example:** 

```json
"John"
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 10  |
| **Max length** | 250 |

## <a name="lastName"></a>3. Property `OF > lastName`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/ofString |

**Description:** last name

**Example:** 

```json
"Doe"
```

**Example:** 

```json
"Doe"
```

| Restrictions   |    |
| -------------- | -- |
| **Min length** | 5  |
| **Max length** | 10 |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
