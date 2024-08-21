# 2024-08-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551628 |       1.00915  |   0.096902 |
| solution-pl        |     0.566433 |       0.108191 |   0.184343 |
| solution-aron-mark |     1.7741   |       0.104743 |   0.188092 |
| solution-1-flask   |     1.06647  |       1.06494  |   0.262615 |
| solution-1         |     7.52407  |       1e-06    |   0.870646 |
| solution-2         |     4.44386  |       0.714247 |   1.09968  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551547 |       1.00893  |   0.197446 |
| solution-pl        |     0.550683 |       0.104287 |   0.295312 |
| solution-aron-mark |     0.549204 |       0.10463  |   0.300575 |
| solution-1-flask   |     0.555039 |       1.00893  |   0.767686 |
| solution-2         |     0.57131  |       0.489037 |   3.1015   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549312 |       1.00902  |   0.909693 |
| solution-pl        |     0.570452 |       0.114938 |   1.01246  |
| solution-aron-mark |     0.562925 |       0.113062 |   1.02083  |
| solution-1-flask   |     0.554843 |       1.00902  |   5.58148  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547967 |       1.00931  |    4.20186 |
| solution-pl        |     0.554989 |       0.144449 |    4.25058 |
| solution-aron-mark |     0.550884 |       0.143779 |    4.29122 |