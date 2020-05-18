#!/usr/bin/env python

# Required imports
import sys
from utils import *
from datetime import datetime

class ConsumerComplaints:
    """
    This class takes csv file path as input, filters data based on given criteria and writes back to another csv file
    
    ...
    
    Attributes
    ----------    


    filtered_content : dictionary
        a dictionary to hold filtered content
    output_list : list
        a list to contain output data
    """
    
    filtered_content = {}    
    output_list = []
    
    def __init__(self, input_filepath, output_filepath):
        """
        Parameters
        ----------
        
        input_filepath : str
            the filepath of input csv file
        output_filepath : str
            the filepath for output csv file
        """
        
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath    
        
    def add_to_filtered_content(self, row):
        """ takes a row as input, filters it and add filtered data to filtered_content
        
        Parameters
        ----------
        
        row : list
            a list including the content of a row
            
        Raises
        ------
        ValueError
            If the date is not in the format of 'YYYY-MM-DD'.
        """
    
        try:
            # extract a year from date string
            year = str(datetime.strptime(row[0], '%Y-%m-%d').date())[:4] 
        except ValueError:
            raise ValueError("Incorrect date format provided, it should be YYYY-MM-DD")       
        
        product = str(row[1]).lower()
        company = str(row[7]).lower()

        # if either product or company name is missing then this row won't be processed
        if not product or not company:
            return
        else:
            product_year = product+"_"+year

            if(product_year in self.filtered_content):
                self.filtered_content[product_year]["# of complaints"] += 1 

                if(company in self.filtered_content[product_year]["# of complaints per company"]):
                    self.filtered_content[product_year]["# of complaints per company"][company] += 1
                else:
                    self.filtered_content[product_year]["# of complaints per company"][company] = 1
            else:
                self.filtered_content[product_year] = {}
                self.filtered_content[product_year]["# of complaints"] = 1
                self.filtered_content[product_year]["# of complaints per company"] = {}
                self.filtered_content[product_year]["# of complaints per company"][company] = 1                
            
    def create_filtered_content(self):
        """  creates full filtered_content dictionary """
        
        for row in read_from_input_file(self.input_filepath):
            self.add_to_filtered_content(row)
    
    def create_output_list(self):
        """ adds filtered data into output list in required format """
        
        for k,v in self.filtered_content.items():
            product_name = k.split("_")[0]            
            
            # if("," in product_name): # adding "" surrounding the products with ',' in them
            #     product_name = '\"' + product_name + '\"'  
                
            year = k.split("_")[1]
            number_of_complaints = v['# of complaints']
            number_of_companies = len(v['# of complaints per company'].values())
            
            # first, sorting companies by # of complaints to get company with highest # of complaints
            # next, dividing that number by total complaints to get required percentage value
            highest_number_of_complaints_in_perc = round((sorted(v['# of complaints per company'].items(), 
                                                      key=lambda x:x[1], reverse=True)[0][1] / number_of_complaints)*100)
            
            self.output_list.append([product_name, year, number_of_complaints, number_of_companies, 
                                highest_number_of_complaints_in_perc])
            

    def generate_output_file(self):
        """ generates required output file by putting all functions together """

        self.create_filtered_content()
        self.create_output_list()
        self.output_list_sorted = sort_output_list(self.output_list)
        write_to_output_file(self.output_filepath, self.output_list_sorted)


# command line arguments
input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

# process input and generate output
cc = ConsumerComplaints(input_filepath, output_filepath)
cc.generate_output_file()