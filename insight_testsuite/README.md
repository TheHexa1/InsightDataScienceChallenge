This folder includes test datasets.

* `test_1`: same as provided in Insight's Challenge repository
* `test_2`: This test case tests for correct date format. It contains complaints.csv with 'Date Received' in "dd-mm-yy" format. This would give error if you run consumer_complaints.py 
        on this input file. Correct date format should be "yyyy-mm-dd" as given in test csv provided by Insight. There is no `output` folder as 
        `consumer_complaints.py` will raise a `ValueError` for this input file.
* `test_3`: This test case tests for missing values in 'company' column. 'input' folder has complaints.csv in which some 
        company names are missing. My code will ignore the rows which have missing values in either company or product. 
        'output' folder contains report.csv with correct output when there are missing values in company column.
* `test_4`: Same as `test_3`, this test case tests for missing values in 'product' column. `input` folder has complaints.csv in which some 
        product names are missing. My code will ignore the rows which have missing values in either company or product. 
        `output` folder contains report.csv with correct output when there are missing values in company column.
    
        
