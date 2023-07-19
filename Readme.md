# Description
Script that helps compare 2 JSON files and bring out a JSON path for each.

# HOW TO USE
1. Place 2 valid JSON files in the project folder
2. Name them `file1.json` and `file2.json`
3. Add unwanted keys to the list `ignored_keys`
4. Run the script

# Known Issues
If you have the same values in different keys, they will be matched. In this case, the result will have to be viewed 
in 4 eyes. %_% I did not become attached to the same names, because they may be different or slightly different. 

# Usage example

```
------------------------------------------------  
Matched Value: 1  
JSON Path - file1.json: body.value  
JSON Path - file2.json: body.path.0.path.value  
------------------------------------------------
```

