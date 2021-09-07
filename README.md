# Safe Website Analysis For Kids


## Usage
>check website

```python
import swafk

url = ""
title = ""
description = ""
rating = ""
keyword = ""

print(swafk.check(url, title, description, keyword, rating))
#good -> if website safe
#bad -> if website not safe
```
\n\n
>print matrix
```python
swafk.matrix(url, title, description, keyword, rating)
# [url]
# fword	 : good
# proflib	 : good
# ipdomain	 : bad
# 
# [title]
# fword	 : good
# proflib	 : good
# 
# [description]
# fword	 : good
# proflib	 : good
# 
# [keyword]
# fword	 : good
# proflib	 : good
# 
# [rating]
# rating	 : good
```
