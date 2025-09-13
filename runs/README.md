# 2025-09-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.479019 |       1.00821  |   0.101249 |
| solution-aron-mark |     0.476746 |       0.153579 |   0.236189 |
| solution-pl        |     5.85194  |       0.31548  |   0.242191 |
| solution-1-flask   |     1.26227  |       1.11006  |   0.269618 |
| solution-1         |     8.38293  |       1e-06    |   0.77226  |
| solution-2         |     0.478367 |       0.750873 |   1.28123  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480521 |       0.156346 |   0.36581  |
| solution-aron-mark |     0.481569 |       0.161638 |   0.366131 |
| solution-flask     |     0.483586 |       1.00843  |   0.404473 |
| solution-1-flask   |     0.485268 |       1.00826  |   0.805955 |
| solution-2         |     0.485279 |       0.505261 |   5.11829  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479211 |       0.15891  |    1.07348 |
| solution-aron-mark |     0.481863 |       0.160666 |    1.07936 |
| solution-flask     |     0.48399  |       1.00857  |    1.58881 |
| solution-1-flask   |     0.490566 |       1.00848  |    5.67411 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478083 |       0.193997 |    3.22579 |
| solution-pl        |     0.483004 |       0.194331 |    3.23998 |
| solution-flask     |     0.480249 |       1.00847  |    5.16134 |