The Broadway dataset contains data for Broadway shows' Capacity (percentage of the theatre filled) and Gross Potential (maximum amount that can be earned) for multiple shows in a specific month and year.

Given a CSV file name read from user input, write a program that performs the following tasks:

Read in the CSV file as a dataframe.
Insert a new column labelled "Size" at the end of the dataframe. The "Size" column contains values in column "Gross Potential" divided by 2.
Output the dataframe using the print() function.
Create a scatter plot of "Gross Potential" vs "Capacity" with the following marker styling parameters:
markers: "x"
color: orange
size: values in column "Size"
Add the x-label ("Capacity", fontsize = 10), y-label ("Gross Potential", fontsize = 10), and title ("Gross Potential vs Capacity", fontsize = 16) to the figure.
Add gridlines to the figure using "--" as linestyle.
Save the figure as output_fig.png.
Run your code at least once before submitting your code for grading. Ensure that output_fig.png exists in the Files pane.

Click here to view Input and Output Example
Ex: If the input is:
broadway_jul_2000.csv
the output using the print() function should be:

     Date.Month  Date.Year  Capacity  Gross Potential  Size
0             7       2000        36               25  12.5
1             7       2000        47               28  14.0
2             7       2000        46               28  14.0
3             7       2000        63               30  15.0
4             7       2000        49               31  15.5
..          ...        ...       ...              ...   ...
122           7       2000       100               97  48.5
123           7       2000       100               97  48.5
124           7       2000       100               98  49.0
125           7       2000       100               98  49.0
126           7       2000        97              121  60.5

[127 rows x 5 columns]

and the output figure (saved in output_fig.png) is:
Alt:
A figure containing a scatter plot of Gross Potential vs Capacity of the Broadway dataset. 
The size of each mark is proportional to the value of the Gross Potential.

Link:
https://static-resources.zybooks.com/zyLab/Python/output_fig_scatterplot1.png


html:
<html style="height: 100%;">
  <head>
    <meta name="viewport" content="width=device-width, minimum-scale=0.1">
    <title>output_fig_scatterplot1.png (640×480)</title>
  </head>
  <body style="margin: 0px; 
    height: 100%; 
    background-color: rgb(14, 14, 14);">
    <img style="display: block;
      -webkit-user-select: none;
      margin: auto;
      background-color: hsl(0, 0%, 90%);
      transition: background-color 300ms;
      " src="https://static-resources.zybooks.com/zyLab/Python/output_fig_scatterplot1.png">
  </body>
</html>
