# 2025-08-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.46548  |       1.04304  |   0.098729 |
| solution-pl        |     0.540153 |       0.16267  |   0.242046 |
| solution-aron-mark |     4.76746  |       0.156811 |   0.245079 |
| solution-1-flask   |     0.534771 |       1.00843  |   0.264913 |
| solution-1         |     8.22278  |       1e-06    |   0.713077 |
| solution-2         |     0.518316 |       0.622813 |   1.58735  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535378 |       0.167665 |   0.373704 |
| solution-flask     |     0.538213 |       1.00886  |   0.381477 |
| solution-aron-mark |     0.552937 |       0.163428 |   0.381505 |
| solution-1-flask   |     0.559604 |       1.00892  |   0.810587 |
| solution-2         |     0.556116 |       0.57042  |   3.20467  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.533403 |       0.179203 |    1.07737 |
| solution-aron-mark |     0.541638 |       0.171454 |    1.10333 |
| solution-flask     |     0.547199 |       1.009    |    1.63855 |
| solution-1-flask   |     0.550437 |       1.00871  |    5.75226 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534329 |        0.19857 |    3.34844 |
| solution-pl        |     0.531212 |        0.19645 |    3.3759  |
| solution-flask     |     0.537447 |        1.00965 |    5.33562 |