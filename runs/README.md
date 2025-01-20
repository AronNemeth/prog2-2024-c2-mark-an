# 2025-01-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.28393  |       1.0086   |   0.081165 |
| solution-pl        |     0.541885 |       0.113623 |   0.17849  |
| solution-aron-mark |     0.551799 |       0.113944 |   0.180198 |
| solution-1-flask   |     5.85247  |       1.06364  |   0.277132 |
| solution-1         |     8.39349  |       2e-06    |   0.594994 |
| solution-2         |     0.550737 |       0.589553 |   0.974445 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.56125  |       0.116689 |   0.277095 |
| solution-aron-mark |     0.540863 |       0.117802 |   0.278461 |
| solution-flask     |     0.546515 |       1.00903  |   0.287048 |
| solution-1-flask   |     0.533818 |       1.00919  |   0.787849 |
| solution-2         |     0.546599 |       0.502967 |  23.0757   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541589 |       0.123486 |   0.87343  |
| solution-aron-mark |     0.553318 |       0.125859 |   0.880605 |
| solution-flask     |     0.530237 |       1.00921  |   1.28212  |
| solution-1-flask   |     0.564181 |       1.00899  |   5.87178  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543401 |       0.152088 |    2.85596 |
| solution-aron-mark |     0.568915 |       0.151006 |    2.91283 |
| solution-flask     |     0.542223 |       1.00916  |    4.38933 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.55828  |       0.259076 |    17.5197 |
| solution-pl        |     0.528459 |       0.249082 |    18.0615 |