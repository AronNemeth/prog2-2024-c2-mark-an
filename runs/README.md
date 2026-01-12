# 2026-01-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.50085  |       1.07698  |   0.100368 |
| solution-pl        |     0.464431 |       0.159506 |   0.24114  |
| solution-aron-mark |     0.472448 |       0.159852 |   0.244711 |
| solution-1-flask   |     0.467313 |       1.00803  |   0.266809 |
| solution-2         |     4.45756  |       0.790422 |   0.890237 |
| solution-1         |     7.44906  |       1e-06    |   0.935262 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462684 |       0.161435 |   0.355013 |
| solution-aron-mark |     0.465137 |       0.161144 |   0.357827 |
| solution-flask     |     0.462499 |       1.00815  |   0.404241 |
| solution-1-flask   |     0.466817 |       1.00816  |   0.78583  |
| solution-2         |     0.465533 |       0.5008   |  11.605    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464391 |       0.167494 |    1.04543 |
| solution-aron-mark |     0.464928 |       0.168195 |    1.04767 |
| solution-flask     |     0.480235 |       1.00821  |    1.55863 |
| solution-1-flask   |     0.472223 |       1.0083   |    5.59261 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.466431 |       0.190861 |    3.37124 |
| solution-aron-mark |     0.465019 |       0.191023 |    3.386   |
| solution-flask     |     0.4649   |       1.00802  |    4.97803 |