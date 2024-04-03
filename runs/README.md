# 2024-04-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.56303  |       1.09729  |   0.067848 |
| solution-pl        |     0.682036 |       0.112995 |   0.167159 |
| solution-aron-mark |     0.704753 |       0.111898 |   0.168596 |
| solution-1-flask   |     0.69855  |       1.00935  |   0.262037 |
| solution-1         |     7.91891  |       1e-06    |   0.620993 |
| solution-2         |     4.69755  |       0.440796 |   1.10892  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.684334 |       1.00905  |   0.171927 |
| solution-pl        |     0.67244  |       0.11873  |   0.260469 |
| solution-aron-mark |     0.681034 |       0.117882 |   0.263387 |
| solution-1-flask   |     0.705724 |       1.00927  |   0.792612 |
| solution-2         |     0.683167 |       0.44355  |   3.24096  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.71806  |       0.12414  |   0.832211 |
| solution-pl        |     0.683396 |       0.122672 |   0.834225 |
| solution-flask     |     0.686699 |       1.00872  |   0.958911 |
| solution-1-flask   |     0.686042 |       1.00909  |   5.62798  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.684537 |       0.156933 |    3.38408 |
| solution-pl        |     0.679171 |       0.157115 |    3.38951 |
| solution-flask     |     0.676406 |       1.00903  |    5.46753 |