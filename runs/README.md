# 2025-12-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.33657  |       1.07358  |   0.101901 |
| solution-aron-mark |     0.475534 |       0.161199 |   0.246287 |
| solution-pl        |     0.46994  |       0.161646 |   0.248345 |
| solution-1-flask   |     0.480927 |       1.00831  |   0.270122 |
| solution-1         |     9.3423   |       1e-06    |   0.68602  |
| solution-2         |     6.07013  |       0.626134 |   0.917471 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476869 |       0.162685 |   0.375478 |
| solution-aron-mark |     0.484973 |       0.165415 |   0.376713 |
| solution-flask     |     0.471562 |       1.00858  |   0.37936  |
| solution-1-flask   |     0.490804 |       1.00865  |   0.795988 |
| solution-2         |     0.467325 |       0.506637 |  12.1211   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476179 |       0.168758 |    1.10536 |
| solution-pl        |     0.475435 |       0.17247  |    1.11095 |
| solution-flask     |     0.474659 |       1.00845  |    1.60674 |
| solution-1-flask   |     0.481173 |       1.00869  |    5.73325 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472903 |       0.194813 |    3.55766 |
| solution-aron-mark |     0.473599 |       0.200115 |    3.73057 |
| solution-flask     |     0.486665 |       1.00852  |    5.15974 |