# 2025-08-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.10833  |       1.05131  |   0.105282 |
| solution-aron-mark |     4.5412   |       0.159342 |   0.241698 |
| solution-pl        |     0.485511 |       0.152657 |   0.245336 |
| solution-1-flask   |     0.498946 |       1.00825  |   0.270148 |
| solution-1         |     8.2105   |       1e-06    |   0.688448 |
| solution-2         |     0.500944 |       0.695558 |   0.821098 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.483037 |       0.155133 |   0.367678 |
| solution-aron-mark |     0.488685 |       0.158913 |   0.375633 |
| solution-flask     |     0.499171 |       1.0087   |   0.38016  |
| solution-1-flask   |     0.485223 |       1.00844  |   0.821045 |
| solution-2         |     0.481443 |       0.505269 |   3.09833  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488214 |       0.160399 |    1.09721 |
| solution-aron-mark |     0.47943  |       0.160745 |    1.11395 |
| solution-flask     |     0.492782 |       1.0085   |    1.59393 |
| solution-1-flask   |     0.484598 |       1.00846  |    5.70748 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47952  |       0.193565 |    3.20411 |
| solution-pl        |     0.478553 |       0.18928  |    3.23324 |
| solution-flask     |     0.482081 |       1.00852  |    5.02893 |