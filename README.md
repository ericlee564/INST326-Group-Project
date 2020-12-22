# INST326-Group-Project
Files:
    finalproject.py: Python script that allows the user to create a dataframe of their inventory using two files that are entered via command line arguments. 

    inventory.csv: A csv that contains the inventory of a store that has columns that include category, item name, amount, and price. It is used in the class and for a majority of the methods. This file has sample data that are used to test and run the program.

    Item_sold.csv: A csv file that contains the data of items sold for a store and has columns for the item name and amount sold. This csv file is used to update the inventory dataframe. The file has sample data for the items represented in the inventory.csv file that are used to test and run the program. 


Command Line Instructions:
    The program runs from a command line argument that contains two csv files, one of which has the inventory data of a store and the other that has the items sold and their amounts. 


How to Use Program/Interpret Results:
    After running the command line argument, the user will be faced with choices on what to be prompted to. This different capabilities represent methods that are in the class, and the user can choose to do different tasks with the options. The user will type in the number representing the task they want to do. 

    After the user selects their prompt, depending on the selection, they will either be provided a dataframe or an input option. For the input option, the user follows the prompt. A dataframe representing the user's desired information is the output. 


Bibliography
    Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
        We used the Pandas documentation for assistance with the module and to better understand the capabilities Pandas has including:
            Subtracting and multiplying columns 
            Filtering 
            Merging

    Pandas Filtering Data frames: https://umd.instructure.com/courses/1288445/quizzes/1381192?module_item_id=10350868 
        We used Pandas in order to filter through a data frame and to merge data frames to combine two relating columns within that data frame. Some of the pandas we used were:
            Filtering and Merging

    Terminal Commands and ArgParse: https://umd.instructure.com/courses/1288445/quizzes/1365188?module_item_id=10239162
        The course content earlier in the semester helped us to create command line arguments to use our script. 


    Used a youtube video for displaying the content https://www.youtube.com/watch?v=qUYMRiP2KDw
        We get some inspiration from this youtube video about how we want to display the options in our program. We used conditional statements in the main function to display the content of each method.

