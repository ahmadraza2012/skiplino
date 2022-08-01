### Available records in grades Collection
```
{ _id: 1, quizzes: [ 5, 6, 7 ] },
{ _id: 2, quizzes: [ ] },
{ _id: 3, quizzes: [ 3, 8, 9 ] }
```

### What is the result of the following command?
```
db.grades.aggregate(
    [
        { $project:
            { adjustedGrades:
                {
                $map:
                    {
                        input: &quot;$quizzes&quot;,
                        as: &quot;grade&quot;,
                        in: { $add: [ &quot;$$grade&quot;, 2 ] }
                    }
                }
            }
        }
    ]
)
```

### Result

```
{ "_id" : 1, "adjustedGrades" : [ 7, 8, 9 ] }
{ "_id" : 2, "adjustedGrades" : [ ] }
{ "_id" : 3, "adjustedGrades" : [ 5, 10, 11 ] }
```