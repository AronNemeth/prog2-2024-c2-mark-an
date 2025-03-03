# 2025-03-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.530104 |       1.00862  |   0.080543 |
| solution-aron-mark |     2.02906  |       0.149498 |   0.205249 |
| solution-pl        |     0.536921 |       0.14144  |   0.206969 |
| solution-1-flask   |     5.17223  |       1.04388  |   0.262211 |
| solution-1         |     7.46133  |       1e-06    |   0.598962 |
| solution-2         |     0.550054 |       0.576584 |   1.0838   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535464 |       1.00872  |   0.295931 |
| solution-aron-mark |     0.541945 |       0.143016 |   0.304579 |
| solution-pl        |     0.533443 |       0.142753 |   0.30494  |
| solution-1-flask   |     0.536338 |       1.00877  |   0.797594 |
| solution-2         |     0.53628  |       0.503872 |   2.26096  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.532321 |       0.149583 |   0.895203 |
| solution-pl        |     0.532647 |       0.151434 |   0.902233 |
| solution-flask     |     0.534149 |       1.00918  |   1.23157  |
| solution-1-flask   |     0.53951  |       1.00886  |   5.64447  |
| solution-2         |     0.536901 |       0.556534 |  46.3787   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.537554 |       0.178533 |    2.82961 |
| solution-aron-mark |     0.531447 |       0.178009 |    2.84502 |
| solution-flask     |     0.532848 |       1.0099   |    4.17609 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531817 |       0.277845 |    16.995  |
| solution-aron-mark |     0.536761 |       0.286095 |    17.1874 |