# 2025-09-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.512691 |       1.00947  |   0.10471  |
| solution-pl        |     6.41633  |       0.391457 |   0.245518 |
| solution-aron-mark |     0.943604 |       0.154879 |   0.24653  |
| solution-1-flask   |     1.44699  |       1.06994  |   0.278963 |
| solution-1         |     8.35233  |       1e-06    |   0.762287 |
| solution-2         |     0.494788 |       0.694618 |   1.02318  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497335 |       0.160329 |   0.372664 |
| solution-pl        |     0.496988 |       0.163829 |   0.375279 |
| solution-flask     |     0.502423 |       1.0094   |   0.396626 |
| solution-1-flask   |     0.50055  |       1.0093   |   0.809675 |
| solution-2         |     0.498275 |       0.513872 |   3.66877  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.499363 |       0.169461 |    1.11498 |
| solution-aron-mark |     0.496574 |       0.171329 |    1.12467 |
| solution-flask     |     0.496148 |       1.00951  |    1.65995 |
| solution-1-flask   |     0.502411 |       1.00956  |    5.79016 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486925 |       0.205199 |    3.38989 |
| solution-pl        |     0.497037 |       0.200416 |    3.39674 |
| solution-flask     |     0.492849 |       1.00967  |    5.20658 |