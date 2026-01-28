# 2026-01-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68569  |       1.05906  |   0.10443  |
| solution-pl        |     0.47764  |       0.167108 |   0.249133 |
| solution-aron-mark |     0.481628 |       0.164295 |   0.250618 |
| solution-1-flask   |     0.477959 |       1.00813  |   0.263186 |
| solution-2         |     4.96081  |       0.680036 |   0.754428 |
| solution-1         |     7.94369  |       1e-06    |   0.807505 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472752 |       0.163531 |   0.370825 |
| solution-flask     |     0.472385 |       1.00829  |   0.374855 |
| solution-pl        |     0.480374 |       0.164539 |   0.375355 |
| solution-1-flask   |     0.480364 |       1.00839  |   0.788631 |
| solution-2         |     0.489052 |       0.524564 |   2.77196  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48095  |       0.170894 |    1.08852 |
| solution-aron-mark |     0.481266 |       0.173815 |    1.09367 |
| solution-flask     |     0.479654 |       1.00871  |    1.61811 |
| solution-1-flask   |     0.482148 |       1.00859  |    5.6041  |
| solution-2         |     0.473985 |       0.564795 |   28.4243  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.485533 |       0.192662 |    3.5957  |
| solution-aron-mark |     0.485234 |       0.193903 |    3.63878 |
| solution-flask     |     0.479389 |       1.00876  |    5.17802 |