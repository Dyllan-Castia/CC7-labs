Given two CSV files containing data for Broadway shows' Capacity (percentage of the theatre filled) and Gross Potential (maximum amount that can be earned) for multiple shows in a specific month:

Read in each CSV file as dataframes.
Print each dataframe individually with a separate print function, one print function per dataframe.
Generate an image containing two scatter subplots comparing that month's Capacity and Gross Potential.
The main title of the image should be "Capacity vs. Gross Potential", with each subplot's title being the month and year, respectively (i.e. "July 2002").
The left subplot should be July's, with the right subplot being December's.
The x-axis should be "Gross Potential" with the y-axis being "Capacity".
Run your code at least once before submitting your code for grading. Ensure that subplots.png exists in the Files pane.

Click here to view Input and Output Example
Ex. If the input is:


broadway_jul_2002.csv
broadway_dec_2002.csv
The output using the print functions should be:

     Month  Year  Capacity  Gross Potential
0        7  2002        39               22
1        7  2002        34               23
2        7  2002        46               29
3        7  2002        38               29
4        7  2002        40               30
..     ...   ...       ...              ...
99       7  2002        97               92
100      7  2002        99              108
101      7  2002        99              109
102      7  2002        99              109
103      7  2002        99              109

[104 rows x 4 columns]
     Month  Year  Capacity  Gross Potential
0       12  2002        30               20
1       12  2002        28               20
2       12  2002        25               24
3       12  2002        58               25
4       12  2002        31               26
..     ...   ...       ...              ...
128     12  2002        91              102
129     12  2002        98              109
130     12  2002       100              110
131     12  2002       100              111
132     12  2002        99              112

[133 rows x 4 columns]

and the output figure (saved in subplots.png) is:
Alt:
An image containing two scatter plots comparing a particular month's capacity versus gross potential.

Link:
https://static-resources.zybooks.com/zyLab/Python/subplots2.png

html:
<html style="height: 100%;">
  <head>
    <meta name="viewport" content="width=device-width, minimum-scale=0.1">
    <title>subplots2.png (640×480)</title>
  </head>
  <body style="margin: 0px; 
    height: 100%; 
    background-color: rgb(14, 14, 14);">
    <img style="display: block;
      -webkit-user-select: none;
      margin: auto;
      background-color: hsl(0, 0%, 90%);
      transition: background-color 300ms;
      " src="https://static-resources.zybooks.com/zyLab/Python/subplots2.png">
  </body>
</html>
