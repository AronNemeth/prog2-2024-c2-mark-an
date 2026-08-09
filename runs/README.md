# 2026-08-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.3985   |       1.0085   |   0.103706 |
| solution-aron-mark |     0.430765 |       0.150865 |   0.238252 |
| solution-pl        |     0.434989 |       0.157044 |   0.239002 |
| solution-1-flask   |     1.201    |       1.06781  |   0.266229 |
| solution-1         |     7.70546  |       1e-06    |   0.646624 |
| solution-2         |     4.58221  |       0.603045 |   1.45359  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427346 |       0.15611  |   0.372209 |
| solution-aron-mark |     0.424456 |       0.155034 |   0.375612 |
| solution-flask     |     0.430742 |       1.00861  |   0.405811 |
| solution-1-flask   |     0.430521 |       1.00875  |   0.801162 |
| solution-2         |     0.429568 |       0.510648 |   3.83846  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431491 |       0.156508 |    1.1214  |
| solution-pl        |     0.430361 |       0.158194 |    1.12609 |
| solution-flask     |     0.431024 |       1.00856  |    1.65482 |
| solution-1-flask   |     0.433278 |       1.00859  |    5.67015 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425508 |       0.186593 |    3.56085 |
| solution-aron-mark |     0.43207  |       0.18198  |    3.57806 |
| solution-flask     |     0.425838 |       1.0092   |    5.35983 |