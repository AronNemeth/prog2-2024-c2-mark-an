# 2026-07-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.19505  |       1.23531  |   0.101848 |
| solution-1-flask   |     0.431452 |       1.00923  |   0.230603 |
| solution-aron-mark |     0.433085 |       0.154019 |   0.23076  |
| solution-pl        |     0.424999 |       0.153587 |   0.23125  |
| solution-1         |     9.24155  |       1e-06    |   0.628542 |
| solution-2         |     5.00173  |       0.607188 |   0.66998  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426721 |       0.152204 |   0.349069 |
| solution-aron-mark |     0.424099 |       0.153401 |   0.356036 |
| solution-flask     |     0.444892 |       1.00967  |   0.408143 |
| solution-1-flask   |     0.429718 |       1.00922  |   0.730814 |
| solution-2         |     0.421079 |       0.497072 |   3.15432  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.424299 |       0.158435 |    1.02224 |
| solution-aron-mark |     0.427752 |       0.156262 |    1.02781 |
| solution-flask     |     0.424088 |       1.0092   |    1.64316 |
| solution-1-flask   |     0.435939 |       1.00915  |    5.66145 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430712 |       0.185002 |    3.86506 |
| solution-aron-mark |     0.427583 |       0.183665 |    3.89136 |
| solution-flask     |     0.442587 |       1.00919  |    5.20073 |