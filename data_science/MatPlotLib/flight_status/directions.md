The LAX dataset contains the flight status at the Los Angeles International Airport in a given year and has the following column labels: Month, Cancelled, Delayed, Diverted, and On Time.

Given a CSV file name read from user input, write a program that performs the following tasks:

Read in the CSV file as a dataframe.
Output the average of flight delays and the average of flight cancellations, with two digits after the decimal point. Follow the output format in the example below.
Create a lineplot of the number of flights delayed each month. Label the plot "Delays".
In the same figure, create another lineplot of the number of flights cancelled each month. Label the plot "Cancellations".
Add the x-label ("Months", fontsize = 10), y-label ("Number of flights", fontsize = 10), title ("Flight status at LAX", fontsize = 14), and a legend to the figure.
Save the figure as output_fig.png.
Run your code at least once before submitting your code for grading. Ensure that output_fig.png exists in the Files pane.

Click here to view Input and Output Example
If the input is:
LAX_2004.csv
the output is:

Average delays: 3309.64
Average cancellations: 215.18

and the output figure (saved in output_fig.png) is:
Alt:
A figure containing a lineplot of flight delays vs months and a lineplot of flight cancellations vs months.

link:
https://static-resources.zybooks.com/zyLab/Python/output_fig_lineplot.png

html:
    <html style="height: 100%;">
    <head>
    <meta name="viewport" content="width=device-width, minimum-scale=0.1">
    <title>output_fig_lineplot.png (640×480)</title>
    </head>
    <body style="margin: 0px; height: 100%; background-color: rgb(14, 14, 14);">
    <img style="display: block;
      -webkit-user-select: none;
      margin: auto;
      background-color: hsl(0, 0%, 90%);
      transition: background-color 300ms;
      " src="https://static-resources.zybooks.com/zyLab/Python/output_fig_lineplot.png">
      </body>
      </html>
