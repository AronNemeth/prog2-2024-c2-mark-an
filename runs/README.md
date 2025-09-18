# 2025-09-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.481096 |       1.00814  |   0.100885 |
| solution-pl        |     6.21735  |       0.189511 |   0.240204 |
| solution-aron-mark |     0.475763 |       0.151924 |   0.240612 |
| solution-1-flask   |     1.18316  |       1.08101  |   0.266415 |
| solution-1         |     8.07184  |       1e-06    |   0.663677 |
| solution-2         |     0.479101 |       0.621333 |   0.866115 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480066 |       0.152919 |   0.360873 |
| solution-aron-mark |     0.483607 |       0.158056 |   0.366868 |
| solution-flask     |     0.479373 |       1.00932  |   0.379879 |
| solution-1-flask   |     0.487253 |       1.0083   |   0.808701 |
| solution-2         |     0.479968 |       0.550977 |   5.66887  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477498 |       0.160908 |    1.0827  |
| solution-aron-mark |     0.480423 |       0.169527 |    1.08376 |
| solution-flask     |     0.483204 |       1.0084   |    1.57356 |
| solution-1-flask   |     0.483693 |       1.00821  |    5.60974 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482257 |       0.189193 |    3.27198 |
| solution-aron-mark |     0.477252 |       0.195293 |    3.31941 |
| solution-flask     |     0.483955 |       1.00858  |    5.17488 |