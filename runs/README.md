# 2025-01-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.43289  |       1.23822  |   0.081152 |
| solution-pl        |     5.02358  |       0.144188 |   0.210005 |
| solution-aron-mark |     0.567634 |       0.147801 |   0.210979 |
| solution-1-flask   |     0.560152 |       1.00928  |   0.283088 |
| solution-1         |     8.25203  |       1e-06    |   0.745055 |
| solution-2         |     0.560976 |       0.659136 |   1.55593  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.568311 |       1.00959  |   0.297961 |
| solution-pl        |     0.561241 |       0.144938 |   0.311881 |
| solution-aron-mark |     0.585922 |       0.145718 |   0.314097 |
| solution-1-flask   |     0.56306  |       1.00888  |   0.814115 |
| solution-2         |     0.554781 |       0.525188 |   8.3709   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.554965 |       0.161019 |   0.912782 |
| solution-aron-mark |     0.569773 |       0.15324  |   0.913437 |
| solution-flask     |     0.547885 |       1.00914  |   1.25488  |
| solution-1-flask   |     0.567321 |       1.00941  |   5.81852  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.559592 |       0.18152  |    2.96201 |
| solution-aron-mark |     0.549839 |       0.179293 |    2.99047 |
| solution-flask     |     0.577291 |       1.00937  |    4.36512 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.556234 |       0.288544 |    18.8823 |
| solution-aron-mark |     0.554598 |       0.286334 |    19.0516 |