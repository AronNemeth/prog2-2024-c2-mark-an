# 2025-08-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.72871  |       1.14195  |   0.100873 |
| solution-pl        |     0.488451 |       0.153623 |   0.236101 |
| solution-aron-mark |     4.99796  |       0.1531   |   0.240529 |
| solution-1-flask   |     0.490906 |       1.00853  |   0.268265 |
| solution-1         |     7.8414   |       1e-06    |   0.838782 |
| solution-2         |     0.59629  |       0.869946 |   1.24616  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498126 |       0.155422 |   0.376721 |
| solution-aron-mark |     0.512822 |       0.16426  |   0.377945 |
| solution-flask     |     0.488075 |       1.00845  |   0.381712 |
| solution-1-flask   |     0.512338 |       1.00961  |   0.82471  |
| solution-2         |     0.492534 |       0.516103 |   5.07317  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488015 |       0.16466  |    1.08354 |
| solution-aron-mark |     0.500078 |       0.162906 |    1.10689 |
| solution-flask     |     0.490778 |       1.00922  |    1.59269 |
| solution-1-flask   |     0.49595  |       1.00848  |    5.76206 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.488597 |       0.191613 |    3.28566 |
| solution-pl        |     0.48921  |       0.192189 |    3.289   |
| solution-flask     |     0.51045  |       1.01192  |    5.1521  |