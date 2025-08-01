# DSCI 523: Programming for Data Manipulation

Program design and data manipulation using industry-standard software tools designed for statistical work. Organizing, filtering, sorting, grouping, reformatting, converting, and cleaning data to prepare it for further analysis. This course is not eligible for Credit/D/Fail grading.

**Course Webpage** <https://pages.github.ubc.ca/MDS-2024-25/DSCI_523_r-prog_students/README.html>

**Course GitHub repo** <https://github.ubc.ca/MDS-2024-25/DSCI_523_r-prog_students>

## License

© 2021 Tiffany Timbers

Software licensed under the MIT License, non-software content licensed under [the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.

## Course Learning Outcomes

By the end of the course, students are expected to be able to:
 
1. Read data into R from vanilla (e.g., `.csv`) and non-standard plain text files, as well as common spreadsheet file types (e.g., `.xls`).

1. Manipulate a single data table in R, to do things such as:
    - filtering rows based on a criterion or combination of criteria;
    - selecting variables;
    - creating new variables and modifying pre-existing ones;
    - rearranging the observations or variables in a deliberate way (e.g., sorting).

1. Define tidy data and explain why it is an optimal format for data analysis involving rectangular data in R.

1. Transform data into the tidy data format in R using `tidyr`. 

1. Understand the key data structures in R.

1. Compare and contrast these relationships to the relationship between `vectors` and `data.frame` objects in R. Move data fluidly between these object types.

1. Manage and manipulate data with dates and times, missing values and categorical variables in R. Rename data frame columns.

1. Work with more than one table (as either separate or nested data structures) in R.

1. Translate fundamental programming concepts such as loops and conditionals into R code.

1. Use the split-apply-combine approach in R to iterate over and summarize data by groups.

1. Understand how to write functions in R, document them correctly and assess if they are correct via unit testing.

1. Know when and how to abstract code (e.g., into functions) to make it more modular and robust.

1. Use a functional programming style as another means of code abstraction in R.

1. Use metaprogramming (in particular, tidy evaluation) to make use of tidyverse functions inside custom written functions in R.

1. Produce human-readable code that incorporates best practices of programming and coding style.


## Teaching Team

### Section 001
| Position                 | Name                     | Slack Handle                |
| :---:                    | :---:                    | :---:                       |     
| Lecture & Lab Instructor | Tiffany Timbers | @tiff |
| Teaching Assistant      | Samir Damji | @Samir Damji |
| Teaching Assistant      | Maria Stephenson | @Maria |
| Teaching Assistant      | Ramin Rezaeianzadeh | @Ramin Rezaeianzadeh (TA) |
| Teaching Assistant      | Riya Eliza Shaju | @Riya Eliza Shaju |

### Section 002
| Position                 | Name                     | Slack Handle                |
| :---:                    | :---:                    | :---:                       |     
| Lecture & Lab Instructor | Gittu George | @gittu |
| Teaching Assistant      | Meltem Omur | @Meltem Omur (TA) |
| Teaching Assistant      | Tony Liang | @Tony Liang |
| Teaching Assistant      | Atabak Eghbal | @Atabak |
| Teaching Assistant      | Ngoc Bui | @ngoc |

## Lecture Schedule

We will be employing a lot of active learning in this course, as you learn programming best by doing! Typically there will be assigned readings & videos that should be reviewed before each lecture. During synchronous lecture meeting times, I will start with a live demonstration related to the videos you watched beforehand, and then we will work in small breakout groups on a lecture worksheet (a Jupyter notebook) that allow us to practice what was covered in the assigned readings & videos. This synchronous class will be recorded and shared afterwards.

|   Lecture  | Topic | Required readings | Required videos | Supplementary resources |
|------------|------|-----|------|-----|
| 1 | Reading data, single data frame manipulations & tidying data in R | <ul>[Introduction to Data Science](https://ubc-dsci.github.io/introduction-to-datascience/)<li>[chapter 1](https://ubc-dsci.github.io/introduction-to-datascience/)</li><li>[chapter 2, sections 2.0-2.5 inclusive](https://ubc-dsci.github.io/introduction-to-datascience/reading.html)</li><li>[chapter 3, sections 3.0-3.5 inclusive](https://ubc-dsci.github.io/introduction-to-datascience/wrangling.html)</li></ul> | [Lecture 1 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[Data Import Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/data-import.pdf)</li><li>[Data transformation cheat sheet](https://github.com/rstudio/cheatsheets/raw/master/data-transformation.pdf)</li><li>[STAT 545 (chapter 5)](https://stat545.com/basic-data-care.html)</li><li>[Relevant chapters of R for Data Science](https://r4ds.had.co.nz/)</li></ul> |
| 2 | Key datatypes & operators in R | Not applicable | [Lecture 2 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[Base R cheat sheet](http://github.com/rstudio/cheatsheets/raw/master/base-r.pdf)</li><li>[Advanced R (chapters 2-5)](https://adv-r.hadley.nz/)</li></ul> |
| 3 | Working with dates, strings & factors in R | [STAT 545 (Data Analysis 2 section)](https://stat545.com/factors-boss.html) | [Lecture 3 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[Dates and Times Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/lubridate.pdf)</li><li>[Work with Strings Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/strings.pdf)</li><li>[Factors with forcats Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/factors.pdf)</ul> | 
| 4 | Two table joins & base R control flow | [STAT 545 (Chapter 15) ](https://stat545.com/join-cheatsheet.html) | [Lecture 4 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | [R for Data Science (chapter 13)](https://r4ds.had.co.nz/relational-data.html) |
| 5 | Tidy control flow in R | [STAT 545 (section 7.8)](https://stat545.com/dplyr-single.html#group_by-is-a-mighty-weapon) | [Lecture 5 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[R for Data Science (section 5.6)](https://r4ds.had.co.nz/transform.html#grouped-summaries-with-summarise)</li></ul> |
| 6 | Functions & testing in R | [R for Data Science (chapter 19)](https://r4ds.had.co.nz/functions.html) | [Lecture 6 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[ Chapters 6 - 8 of Advanced R](https://adv-r.hadley.nz/functions.html) </li><li>[Testing chapter of R packages](https://r-pkgs.org/tests.html)</li></ul> |
| 7 | Mapping & nested data frames in R | | [Lecture 7 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li> [RStudio Apply/map functions Cheat Sheet](https://github.com/rstudio/cheatsheets/raw/master/purrr.pdf)</li><li>[R for Data Science (section 21.5)](https://r4ds.had.co.nz/iteration.html#the-map-functions)</li><li>[R for Data Science (section 25.3 - 25.5)](https://r4ds.had.co.nz/many-models.html#list-columns-1)</li><li>[Advanced R (chapter 9)](https://adv-r.hadley.nz/fp.html)</li></ul>  |
| 8 | Tidy evaluation in R | [Programming with dplyr](https://dplyr.tidyverse.org/articles/programming.html) | [Lecture 8 videos](https://canvas.ubc.ca/courses/146098/external_tools/42332) | <ul><li>[RStudio Tidy Evaluation Cheat Sheet](https://github.com/rstudio/cheatsheets/raw/master/tidyeval.pdf)</li><li>[Advanced R (Metaprogramming section)](https://adv-r.hadley.nz/metaprogramming.html) |

See the [lecture learning objectives](lec_learning_objectives.md) for a detailed breakdown of lecture-by-lecture learning objectives.  


## Deliverables

You are responsible for the following deliverables, which will determine your course grade:

| Assessment       | Weight  | Due Date         |
| :---:            | :---:   |:---:            |
| Lab 1 | 10%     | 2024-09-07 18:00 PT |
| Lab 2 | 10%     | 2024-09-14 18:00 PT |
| Lab 3 | 10%     | 2024-09-22 11:59 PT |
| Lab 4 | 10%     | 2024-09-28 18:00 PT |
| Worksheet 1 | 1%     | 2024-09-07 18:00 PT |
| Worksheet 2 | 1%     | 2024-09-07 18:00 PT |
| Worksheet 3 | 1%     | 2024-09-14 18:00 PT |
| Worksheet 4 | 1%     | 2024-09-14 18:00 PT |
| Worksheet 5 | 1%     | 2024-09-22 11:59 PT |
| Worksheet 6 | 1%     | 2024-09-22 11:59 PT |
| Worksheet 7 | 1%     | 2024-09-28 18:00 PT |
| Worksheet 8 | 1%     | 2024-09-28 18:00 PT |
| Pre-lecture quizzes | 1% | Before each lecture |
| iClicker    | 1%     | During each lecture |
| Quiz 1           | 25%     | 2024-09-17 - 2024-09-20 |
| Quiz 2           | 25%     | 2024-10-01 - 2024-10-04 |

## Class Schedule & office hours

See [calendar](https://ubc-mds.github.io/calendar/).

## Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).
