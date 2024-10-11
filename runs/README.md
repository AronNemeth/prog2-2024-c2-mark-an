# 2024-10-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30761  |       1.10749  |   0.096421 |
| solution-pl        |     5.7672   |       0.106555 |   0.172022 |
| solution-aron-mark |     0.576265 |       0.106172 |   0.194687 |
| solution-1-flask   |     0.588481 |       1.00891  |   0.258176 |
| solution-1         |     7.81337  |       1e-06    |   0.633097 |
| solution-2         |     0.57523  |       0.514007 |   1.40475  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.579332 |       1.00966  |   0.228949 |
| solution-aron-mark |     0.582942 |       0.115574 |   0.307124 |
| solution-pl        |     0.582223 |       0.106887 |   0.33706  |
| solution-1-flask   |     0.583325 |       1.009    |   0.770916 |
| solution-2         |     0.584827 |       0.49894  |   2.68689  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.57976  |       1.00953  |   0.887032 |
| solution-aron-mark |     0.592736 |       0.115494 |   0.988091 |
| solution-pl        |     0.60823  |       0.118008 |   0.998219 |
| solution-1-flask   |     0.592954 |       1.00903  |   5.47542  |
| solution-2         |     0.580811 |       0.545707 |  43.6838   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.581319 |       1.00954  |    4.52065 |
| solution-aron-mark |     0.575224 |       0.152451 |    4.61749 |
| solution-pl        |     0.578736 |       0.15118  |    4.64516 |