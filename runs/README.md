# 2025-11-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.87517  |       1.04957  |   0.103483 |
| solution-pl        |     0.491901 |       0.156819 |   0.241565 |
| solution-aron-mark |     0.47881  |       0.16166  |   0.249591 |
| solution-1-flask   |     0.48732  |       1.00822  |   0.269092 |
| solution-2         |     4.90026  |       0.888309 |   0.913328 |
| solution-1         |     7.8575   |       1e-06    |   1.13587  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.468894 |       0.157254 |   0.36657  |
| solution-aron-mark |     0.4676   |       0.159075 |   0.371357 |
| solution-flask     |     0.476478 |       1.00847  |   0.386451 |
| solution-1-flask   |     0.472092 |       1.00812  |   0.801309 |
| solution-2         |     0.463307 |       0.504575 |   4.63246  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.479659 |       0.167832 |    1.08305 |
| solution-pl        |     0.488795 |       0.169256 |    1.0878  |
| solution-flask     |     0.472209 |       1.00863  |    1.58175 |
| solution-1-flask   |     0.480376 |       1.00849  |    5.57291 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470047 |       0.196577 |    3.2179  |
| solution-pl        |     0.469269 |       0.19546  |    3.25774 |
| solution-flask     |     0.475255 |       1.00855  |    5.06561 |