# java-python-matpoltlib
Use Java to call Python to draw multiple line charts for data analysis
# The general idea of this process is as follows:
##### 1.Create the data you need to draw a line chart
##### 2. Process the source data in Java. The data is placed in a List and merged into a List. Note that the length of your first list needs to be placed last.
##### 3. Execute the python file through exec, that is, through the cmd command line
##### 4, the Python file needs to get the list parameters from Java for conversion. Convert a javad list into two python lists. (The specific implementation can be seen in the source code)
##### 5. Python plots through matplotlib.
