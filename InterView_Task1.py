"""
******************* Interview Question *******************

Problem 1:

We have a string “input_str”, and input_str can be any alpha-numeric text with length of 10 to 10000.

Example of input_str:
Input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative.”

We have another variable, an array of words called “validation_array”. It can have upto 1000 items.

Example of validation_array:
Validation_array = [“food”, “face”, “donation”, “coalition”, “economy”, “sector”]

We need to identify and print the output that the items in “validation_array” are occurring how many times in input_str.

Example:

input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation”

validation_array = [“food”, “face”, “the”, “donation”, “coalition”, “economy”, “sector”]

output:

food: 1
face: 1
the: 6
donation: 2
coalition: 1
economy: 1
sector: 1

"""

################################################################################################ SOLUTION ...!!! STARTS HERE

import pandas as pd
# Input_str
Input_str  = """
Los Angeles, CA, July 09, 2020 --(PR.com)-- With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted.
DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative."
DMS is donating thousands of reusable facemasks to restaurants across the United States to support and assist them to stay safe as the nation begins to reopen.
Alex Berenson, CEO of DMS Coalition, said: “This is a time where we need to come together to help one another, and we feel assistance should not only be addressed from the government but by the communities we work and live in.”
DMS Coalition has been advocating face masks for all and is proud to be at the forefront in domestically producing a wide array of styles. The washable and reusable face masks assortment includes adult and kids’ masks in a variety of colors and prints.
“We all must do our part to assist and support everyone at this crucial time and it is fitting that DMS is providing for the restaurant industry a small token of appreciation for all that they do,” said Crystal Solorzano, Founder and Chairwoman of DMS Coalition.
Further adding,“When we started DMS Coalition, our initial task was our front-line healthcare warriors, and we are continuing our mission by doing whatever is necessary to put a mask on every single American.”
Please visit www.DMSCoalition.com for more information about the Coalition.
About DMS Coalition:
Domestic Medical Supply was created by and for the community. The American spirit is very much evident in that DMS Coalition has put thousands of hard-working people from the domestic workforce back to work producing essential and critical lifesaving gear. DMS is dedicated network of Factory Coalition partners who manufacture Personal Protective Equipment so desperately needed by the domestic workforce working the front lines. We have created a partnership that brings together healthcare & business leaders, resources and communities so that we Never Again allow global shortages to impede our first responders in the event of catastrophic disasters.
"""

# Validation_array
Validation_array = ["food", "face" , "donation" , "coalition", "economy" , "sector"]

# Solution Code :

def remove_punct(str_x):
    """
    Function to remove all possible puncutations from
    the given Input_str
    """
    punctuations = '''!()-[]{};:'"’”“\,<>./?@#$%^&*_~'''

    no_punct = ""
    for char in str_x:
       if char not in punctuations:
           no_punct = no_punct + char
    return no_punct
# store unpunctuated string in raw data`
raw_data = remove_punct(Input_str)

# Using List Comprehension to get a new list
nl = [i for i in raw_data.lower().replace("\n"," ").split(" ") if i != ""]
# Using pandas to calculate the value count of each words
data = pd.DataFrame({"WORDS":nl})
got = data["WORDS"].value_counts()

# Getting final required result through nested for loop
for i in got.items():
    for j in Validation_array:
        if(i[0]==j):
            print(j , " = " , i[1])
