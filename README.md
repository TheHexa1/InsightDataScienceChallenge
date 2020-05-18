# InsightDataScience Challenge for Data Engineer program

## How to run
* For linux users: Clone this repository and just execute `run.sh`
* For windows users: Clone this repository --> Open cmd --> goto directory where you cloned this repo --> type `python ./src/consumer_complaints.py ./input/complaints.csv ./output/report.csv` in cmd and hit `Enter`

## Summary of my approach

The aim is to process given csv file and to extract data from 3 columns: 'Date received', 'Product' and 'Company'. <br>
<br>
As I am using Python to solve this challenge, I utilized python's inbuilt data structures such as dictionary and list. I am processing each row one by one and storing processed data into a nested dictionary, which is formatted in a specific way so as to extract required data once all data has been processed.<br>
<br>
Once dictionary is created, I am iterating over whole dictionary to extract required data. And appending formatted data into a list. 
I used list so as to utlize its inbuilt sorting function to sort data as required. At the end, I am using csv module to generate report.csv from sorted output list. 
