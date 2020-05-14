## Manual Data Classifier

A web app based on flask for data classification manully.  

You just need to put the source data json file and modified the config.json file, and you can browse your every data item via brower and classified them easily.

### Setup

1. install all requirements
```shell
pip install -r requirements.txt
```

2. fill in `config.json` and put the source data file to `data/source/` directory
3. run the flask app and start your job on [website](http://localhost:5000) 

```shell
python app.py
```

### Configuration

According to your need to modify the `config.json`

```javascript
{
    "sourceDataPath": "data/source/data.json",//source data path
    "itemId": "bug_id", // id used to identify every data item
    "fields": [//which fields to display, if is [] then display all fields
        "bug_id",
        "creation_ts",
        "short_desc",
        "product"
    ],
    "longFields": [ // fields need to display separately, 
        "long_desc" // which will keep the line break and blank
    ],
    "splitFields": [ // fileds containing several parts which
        {            // is separated by split delimiter
            "field": "comment",
            "split": "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        }
    ],
    "result": "data/results.json", // results store path
    "resultOptions": [
        {
            "field": "field1", // type's filed name
            "mutiple": false, // support choose mutiple option
            "options": [ // options which can be choosed
                {
                    "label": "label1", 
                    "value": 1
                },
                {
                    "label": "label2",
                    "value": 2
                }
            ]
        }
    ]
}
```

### result

results is stored as a json file.

```javascript
{
  "12266": {
    "field1": 1,
    "field2": [ // multiple options
      1,
      2
    ]
  }
}
```

### TODO (Maybe)

1. Improve documentation
2. Support import CSV source file and export CSV results
3. A safer approach to save results
4. Concurrently used to classified data by several people 
