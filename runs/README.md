# 2025-02-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.527624 |       1.00899  |   0.080472 |
| solution-pl        |     1.78992  |       0.152491 |   0.205142 |
| solution-aron-mark |     0.53754  |       0.140394 |   0.205886 |
| solution-1-flask   |     5.06489  |       1.12763  |   0.270653 |
| solution-1         |     7.35985  |       1e-06    |   0.640326 |
| solution-2         |     0.531725 |       0.583677 |   0.840462 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.527957 |       1.00916  |   0.292764 |
| solution-aron-mark |     0.5351   |       0.142444 |   0.306843 |
| solution-pl        |     0.529909 |       0.146366 |   0.313297 |
| solution-1-flask   |     0.540066 |       1.00902  |   0.792536 |
| solution-2         |     0.552136 |       0.505907 |  13.1513   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.536464 |       0.149352 |   0.91045  |
| solution-pl        |     0.534605 |       0.150034 |   0.918589 |
| solution-flask     |     0.533897 |       1.00898  |   1.23069  |
| solution-1-flask   |     0.543397 |       1.00897  |   5.64194  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.532877 |       0.179269 |    2.83292 |
| solution-pl        |     0.53218  |       0.177368 |    2.84728 |
| solution-flask     |     0.530009 |       1.00972  |    4.1685  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.5418   |       0.2781   |    17.5803 |
| solution-pl        |     0.530161 |       0.282288 |    17.6418 |