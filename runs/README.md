# 2026-08-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23381  |       1.1158   |   0.103788 |
| solution-1-flask   |     0.434122 |       1.00903  |   0.230738 |
| solution-aron-mark |     0.490195 |       0.172228 |   0.236405 |
| solution-pl        |     6.86112  |       0.290374 |   0.238774 |
| solution-1         |     8.65491  |       1e-06    |   0.85762  |
| solution-2         |     0.452847 |       0.868881 |   0.880013 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427337 |       0.161403 |   0.365304 |
| solution-aron-mark |     0.439502 |       0.160731 |   0.374391 |
| solution-flask     |     0.429408 |       1.00902  |   0.405302 |
| solution-1-flask   |     0.430578 |       1.00904  |   0.73341  |
| solution-2         |     0.425309 |       0.51225  |   2.81038  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.432444 |       0.160618 |    1.05243 |
| solution-pl        |     0.439566 |       0.165192 |    1.05266 |
| solution-flask     |     0.424612 |       1.00923  |    1.66768 |
| solution-1-flask   |     0.443552 |       1.0092   |    5.76262 |
| solution-2         |     0.443786 |       0.607604 |   41.3302  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436844 |       0.186021 |    3.54204 |
| solution-pl        |     0.434271 |       0.190946 |    3.60026 |
| solution-flask     |     0.444434 |       1.00924  |    5.31249 |