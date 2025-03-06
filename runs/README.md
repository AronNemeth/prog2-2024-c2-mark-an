# 2025-03-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550223 |       1.00961  |   0.095166 |
| solution-aron-mark |     1.92088  |       0.148032 |   0.207138 |
| solution-pl        |     0.546594 |       0.143948 |   0.211897 |
| solution-1-flask   |     5.25445  |       1.08125  |   0.272299 |
| solution-1         |     7.67924  |       1e-06    |   0.920002 |
| solution-2         |     0.546036 |       0.939334 |   0.949734 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56339  |       1.00916  |   0.292707 |
| solution-pl        |     0.549373 |       0.151654 |   0.313478 |
| solution-aron-mark |     0.536889 |       0.143599 |   0.313694 |
| solution-1-flask   |     0.554939 |       1.00903  |   0.800824 |
| solution-2         |     0.550046 |       0.504563 |   2.4953   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.555173 |       0.150905 |   0.89597  |
| solution-pl        |     0.545328 |       0.150067 |   0.903752 |
| solution-flask     |     0.543409 |       1.00916  |   1.22404  |
| solution-1-flask   |     0.57004  |       1.00913  |   5.79989  |
| solution-2         |     0.534891 |       0.560636 | 176.73     |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.560197 |       0.180394 |    2.90641 |
| solution-aron-mark |     0.538732 |       0.181202 |    2.9833  |
| solution-flask     |     0.558948 |       1.00926  |    4.20145 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.544359 |       0.283996 |    17.8319 |
| solution-aron-mark |     0.561778 |       0.28831  |    18.8938 |