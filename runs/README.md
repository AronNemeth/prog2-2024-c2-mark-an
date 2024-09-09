# 2024-09-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.55153  |       1.12775  |   0.093308 |
| solution-aron-mark |     6.15519  |       0.107971 |   0.177681 |
| solution-pl        |     0.58028  |       0.105612 |   0.19285  |
| solution-1-flask   |     0.584663 |       1.00927  |   0.262167 |
| solution-1         |     8.59827  |       1e-06    |   0.593087 |
| solution-2         |     0.569571 |       0.58699  |   1.04789  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.572741 |       1.0094   |   0.226326 |
| solution-pl        |     0.57895  |       0.108682 |   0.297587 |
| solution-aron-mark |     0.577801 |       0.108797 |   0.306744 |
| solution-1-flask   |     0.576509 |       1.00957  |   0.788849 |
| solution-2         |     0.582692 |       0.501655 |   4.5188   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.583554 |       1.00943  |   0.892737 |
| solution-aron-mark |     0.586275 |       0.114065 |   1.00331  |
| solution-pl        |     0.574146 |       0.1154   |   1.00825  |
| solution-1-flask   |     0.578029 |       1.00967  |   5.71879  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.565889 |       1.00926  |    4.41142 |
| solution-aron-mark |     0.575116 |       0.147414 |    4.46528 |
| solution-pl        |     0.576977 |       0.145827 |    4.53697 |