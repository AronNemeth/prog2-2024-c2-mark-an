# 2024-09-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.4403   |       1.05896  |   0.085369 |
| solution-aron-mark |     2.00985  |       0.107375 |   0.179383 |
| solution-pl        |     0.570183 |       0.10442  |   0.18492  |
| solution-1-flask   |     0.584625 |       1.00822  |   0.260599 |
| solution-1         |     8.1266   |       1e-06    |   0.814889 |
| solution-2         |     4.69261  |       0.627139 |   1.20579  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.586352 |       1.00825  |   0.213309 |
| solution-aron-mark |     0.583866 |       0.106702 |   0.312645 |
| solution-pl        |     0.583858 |       0.10794  |   0.314194 |
| solution-1-flask   |     0.584841 |       1.00833  |   0.780961 |
| solution-2         |     0.584055 |       0.50174  |   6.9747   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.576215 |       1.00864  |   0.954081 |
| solution-pl        |     0.593873 |       0.113524 |   1.06203  |
| solution-aron-mark |     0.586654 |       0.113892 |   1.06351  |
| solution-1-flask   |     0.598763 |       1.00834  |   5.57498  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.5829   |       1.00841  |    4.55095 |
| solution-aron-mark |     0.588221 |       0.141908 |    4.65932 |
| solution-pl        |     0.58314  |       0.144029 |    4.73888 |