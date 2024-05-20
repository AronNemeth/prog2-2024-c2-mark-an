# 2024-05-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31985  |       1.15503  |   0.075155 |
| solution-pl        |     0.661992 |       0.118543 |   0.173014 |
| solution-aron-mark |     5.83704  |       0.12261  |   0.173975 |
| solution-1-flask   |     0.678304 |       1.00894  |   0.255607 |
| solution-1         |     7.90846  |       1e-06    |   0.590178 |
| solution-2         |     0.658895 |       0.423174 |   1.51013  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664029 |       1.00906  |   0.160933 |
| solution-aron-mark |     0.673543 |       0.124674 |   0.270847 |
| solution-pl        |     0.663401 |       0.126142 |   0.2709   |
| solution-1-flask   |     0.682655 |       1.00913  |   0.779208 |
| solution-2         |     0.659236 |       0.434282 |   2.78918  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.676086 |       1.00866  |   0.68565  |
| solution-aron-mark |     0.668974 |       0.132472 |   0.826198 |
| solution-pl        |     0.688361 |       0.136599 |   0.827587 |
| solution-1-flask   |     0.688406 |       1.00944  |   5.54256  |
| solution-2         |     0.677702 |       0.485229 |  31.5056   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667222 |       1.00943  |    2.48515 |
| solution-pl        |     0.670857 |       0.17112  |    2.61454 |
| solution-aron-mark |     0.675134 |       0.170045 |    2.64331 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.659446 |       0.293265 |    15.6052 |
| solution-aron-mark |     0.66329  |       0.297102 |    15.8653 |
| solution-flask     |     0.67028  |       1.00923  |    16.117  |