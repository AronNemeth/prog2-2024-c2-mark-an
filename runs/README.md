# 2025-08-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68471  |       1.06294  |   0.119193 |
| solution-aron-mark |     5.62823  |       0.166412 |   0.267351 |
| solution-pl        |     0.574331 |       0.170927 |   0.267591 |
| solution-1-flask   |     0.607461 |       1.00925  |   0.280629 |
| solution-1         |     8.89938  |       2e-06    |   0.761369 |
| solution-2         |     0.528113 |       0.83507  |   1.16473  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527169 |       0.164707 |   0.403114 |
| solution-aron-mark |     0.562191 |       0.179565 |   0.422617 |
| solution-flask     |     0.54318  |       1.009    |   0.42303  |
| solution-1-flask   |     0.5466   |       1.00847  |   0.844772 |
| solution-2         |     0.553194 |       0.596322 |   3.64041  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.528091 |       0.175937 |    1.14651 |
| solution-aron-mark |     0.537012 |       0.176131 |    1.14705 |
| solution-flask     |     0.533499 |       1.00946  |    1.76073 |
| solution-1-flask   |     0.540873 |       1.00893  |    6.07365 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.577705 |       0.215605 |    3.96328 |
| solution-pl        |     0.520499 |       0.207752 |    3.96821 |
| solution-flask     |     0.526417 |       1.0093   |    6.13845 |