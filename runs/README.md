# 2026-07-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.89341  |       1.05693  |   0.070008 |
| solution-1-flask   |     0.303629 |       1.00642  |   0.154632 |
| solution-aron-mark |     0.296121 |       0.108608 |   0.155314 |
| solution-pl        |     0.292737 |       0.106535 |   0.162369 |
| solution-1         |     5.71957  |       1e-06    |   0.439677 |
| solution-2         |     3.60851  |       0.486152 |   0.619208 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.297675 |       0.107958 |   0.240464 |
| solution-aron-mark |     0.295413 |       0.107476 |   0.248965 |
| solution-flask     |     0.298678 |       1.00683  |   0.305974 |
| solution-1-flask   |     0.299894 |       1.0066   |   0.490364 |
| solution-2         |     0.294649 |       0.362423 |   1.79435  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.281508 |       0.107814 |   0.754729 |
| solution-aron-mark |     0.282546 |       0.107298 |   0.784706 |
| solution-flask     |     0.286363 |       1.00608  |   1.22183  |
| solution-1-flask   |     0.29419  |       1.00666  |   3.87423  |
| solution-2         |     0.296487 |       0.397958 | 133.897    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.279984 |       0.128583 |    3.2695  |
| solution-pl        |     0.284327 |       0.127112 |    3.30762 |
| solution-flask     |     0.282736 |       1.00621  |    4.09777 |