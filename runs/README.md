# 2024-09-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.40009  |       1.07345  |   0.075319 |
| solution-aron-mark |     6.09215  |       0.103203 |   0.169133 |
| solution-pl        |     0.558334 |       0.10381  |   0.188791 |
| solution-1-flask   |     0.55679  |       1.00882  |   0.258536 |
| solution-1         |     8.69835  |       1e-06    |   0.803193 |
| solution-2         |     0.551549 |       0.615193 |   1.47685  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557369 |       1.00908  |   0.219252 |
| solution-pl        |     0.550223 |       0.104388 |   0.286445 |
| solution-aron-mark |     0.552948 |       0.105014 |   0.316358 |
| solution-1-flask   |     0.553722 |       1.00943  |   0.784108 |
| solution-2         |     0.546769 |       0.482617 |   2.16207  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.544813 |       1.00908  |   0.876003 |
| solution-aron-mark |     0.550965 |       0.112933 |   0.979232 |
| solution-pl        |     0.543242 |       0.111197 |   0.98136  |
| solution-1-flask   |     0.560461 |       1.0092   |   5.51729  |
| solution-2         |     0.559255 |       0.538111 |  29.8182   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561116 |       1.00885  |    4.08098 |
| solution-pl        |     0.546685 |       0.140973 |    4.24984 |
| solution-aron-mark |     0.552078 |       0.145311 |    4.25492 |