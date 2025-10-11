# 2025-10-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68723  |       1.06306  |   0.099915 |
| solution-aron-mark |     0.486979 |       0.158016 |   0.241642 |
| solution-pl        |     0.491488 |       0.156672 |   0.244387 |
| solution-1-flask   |     0.489398 |       1.00812  |   0.265317 |
| solution-1         |     8.21632  |       1e-06    |   0.833681 |
| solution-2         |     5.02797  |       0.760139 |   1.13322  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489167 |       0.156647 |   0.366095 |
| solution-aron-mark |     0.492499 |       0.158798 |   0.369062 |
| solution-flask     |     0.486055 |       1.0084   |   0.37425  |
| solution-1-flask   |     0.508747 |       1.00849  |   0.810703 |
| solution-2         |     0.487906 |       0.510478 |   3.15318  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4875   |       0.163098 |    1.07239 |
| solution-aron-mark |     0.488234 |       0.163875 |    1.07831 |
| solution-flask     |     0.48349  |       1.00851  |    1.57396 |
| solution-1-flask   |     0.492012 |       1.00838  |    5.68558 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.493318 |       0.194459 |    3.26208 |
| solution-aron-mark |     0.48642  |       0.194624 |    3.27631 |
| solution-flask     |     0.489192 |       1.00859  |    5.09382 |