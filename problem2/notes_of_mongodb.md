### Properties 
#### 1. document based: document is a representation of a single entity of data in the MongoDB.  Data stored as binary serializable json objects called bson( field:value pairs).

|NoSQL|Relational DB|
|---|---|
|document|record(row)|
|field|column|
|collection|table|

#### 2. schema-free: doesn't require a pre-defined schema like relational database does.

### Query
####1. Read
|operator|example|
|---|---|
|less than|{'age': {$lt: 20}}|
|greater than|{'age': {$gt: 20}}|
|less than or equal to|{'age': {$lte: 20}}|
|greater than or equal to|{'age': {$gte: 20}}|
|not equal to|{'age': {$ne: 20}}|
|find matched values in an array|{'age': {$in: [20, 23]}}|
|find matched values in an array|tags: { $in: ["appliances", "school"] } |
|find matched values in an array|{ tags: { $in: [ /^be/, /^st/ ] } }  i.e.  either starts with 'be' or 'st'|
