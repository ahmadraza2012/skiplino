## db.collection.find()
Returns the list of documents after filtering which is mentioned in the find command. If there is no document matched with mentioned command, then it will return {} by default.

For Example, let just say we have these documents available.

```
{ "_id": "apples", "qty": 5 }
{ "_id": "bananas", "qty": 7 }
{ "_id": "oranges", "qty": { "in stock": 8, "ordered": 12 } }
{ "_id": "avocados", "qty": "fourteen" }
```

The following command `db.collection.find( { qty: { $gt: 4 } } )` will return those documents where `qty` will be greater than `4`. The these will be resulted documents.

```
{ "_id": "apples", "qty": 5 }
{ "_id": "bananas", "qty": 7 }
```

## db.collection.findOne()

Returns only the first document. after filtering which is mentioned in the find command. Assume the above mentioned example, it will return only first found document. `db.collection.findOne( { qty: { $gt: 4 } } )` 

```
{ "_id": "apples", "qty": 5 }
```


