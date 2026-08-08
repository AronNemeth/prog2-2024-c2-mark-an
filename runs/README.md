# 2026-08-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.09122  |       1.00842  |   0.106503 |
| solution-aron-mark |     0.434336 |       0.156611 |   0.2409   |
| solution-pl        |     0.43712  |       0.151872 |   0.24132  |
| solution-1-flask   |     1.14598  |       1.05754  |   0.274007 |
| solution-1         |     8.27085  |       1e-06    |   0.651422 |
| solution-2         |     4.87442  |       0.669088 |   1.16617  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430424 |       0.156652 |   0.37067  |
| solution-aron-mark |     0.433805 |       0.151447 |   0.372639 |
| solution-flask     |     0.448717 |       1.00884  |   0.396638 |
| solution-1-flask   |     0.462024 |       1.00842  |   0.825234 |
| solution-2         |     0.436723 |       0.53262  |   2.58071  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.435636 |       0.157766 |    1.11067 |
| solution-aron-mark |     0.437192 |       0.15872  |    1.11676 |
| solution-flask     |     0.429103 |       1.00854  |    1.65708 |
| solution-1-flask   |     0.444841 |       1.00871  |    5.69005 |
| solution-2         |     0.432668 |       0.561842 |  167.553   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.43368  |       0.185745 |    3.54076 |
| solution-aron-mark |     0.432551 |       0.185111 |    3.58309 |
| solution-flask     |     0.434707 |       1.00854  |    5.38671 |