# 2025-01-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.82263  |       1.00877  |   0.104289 |
| solution-aron-mark |     0.526313 |       0.107345 |   0.184365 |
| solution-pl        |     0.52864  |       0.108679 |   0.186406 |
| solution-1-flask   |     5.71913  |       1.11572  |   0.264442 |
| solution-1         |     7.73406  |       1e-06    |   0.596468 |
| solution-2         |     0.528712 |       0.52256  |   0.733855 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527476 |       0.111852 |   0.314069 |
| solution-pl        |     0.554146 |       0.114617 |   0.314624 |
| solution-flask     |     0.527347 |       1.00867  |   0.476866 |
| solution-1-flask   |     0.534583 |       1.00877  |   0.803995 |
| solution-2         |     0.526251 |       0.484286 |   3.153    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.5293   |       0.117386 |    1.06116 |
| solution-aron-mark |     0.560348 |       0.1177   |    1.11038 |
| solution-flask     |     0.533566 |       1.00861  |    2.13928 |
| solution-1-flask   |     0.544274 |       1.00873  |    5.85729 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.523539 |       0.143486 |    4.28868 |
| solution-pl        |     0.527463 |       0.142855 |    4.30425 |
| solution-flask     |     0.527066 |       1.00877  |    8.33956 |