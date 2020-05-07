# Answers
- I have tried to answer all of the questions here.
## Part 1: Reconcilation
#### Matching and reconcilation method
- First I read the file and get rows from file.
- first rows are taken as headers, I renamed ID to item_id to make not to confuse with the primary key id.
- then I find the index of ISWC because this is the unique field in this data.
- if ISWC column is empty in a row that row is ignored
- I collected all the rows and keep in a dictionary so that I can find the data for an iswc key
- when new row is found, the item is checked with db whether it exists in database or not.
- if the item with iswc already exist in db, we ignore the row
- if the item is not in db but in the previous row I checked the length of items in both rows and then having more field is selected.
- after that I have created a bulk object list to save all the rows in db
- finally I saved all the rows in db in bulk.

#### Automation of process
- actually I am a bit unclear about this question. We have made a portal in this system as that was my second part of the test. 
- We use that portal to upload the files. But still depending on the requirements and problem of the system we can work on it more. 
- To explain it more, I need to know how frequently we receive the data and the formats and source of data.


## Part 2: API 
#### For Large Datasets
- If the Single View has 20 million musical works, the response time will not be the same in this code.
- There are lots of options to improve the response time. Some of them are caching, creating asynchronous task, and multiprocessing.

#### Caching
- In this situation, there is one place where we can use caching but it may use lots of memory.
- While validating the iswc data from db to make unique iswc, we need to fetch all data from db.
- Fetching all iswc makes the response a bit slower, so we can cache the existing iswc items in reddis or some other caching tools.
- But depending on the situation the caching may not be perfect for this situation.
- To decide further, more system requirement and problem is necessary to know.

### Asynchronous Task with celery
- This is the best option in this situation. If we have large volume in data we can serve them asynchronously and notify later to the user when the operation is successfully completed.
- We can create a multiple batch, so I have added a batch field in my code but not implemented in my existing code.


#### Multiprocessing
- If we have multiple core server, we still have option of multi-processing to refine and validate the data
- The finalized data can be saved in batch as explain above.

#### Conclusion
We can use caching, asynchronous task and multiprocessing with a better combination according the situation and the problem.

####Note
I have not used any authentication because I think the question is not focused on authentication rather the other task.
And also the front-end is not so fancy.