# 2025-01-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85128  |       1.00876  |   0.104998 |
| solution-aron-mark |     0.530263 |       0.108389 |   0.185816 |
| solution-pl        |     0.530869 |       0.11253  |   0.187329 |
| solution-1-flask   |     4.98617  |       1.10287  |   0.265547 |
| solution-1         |     7.49898  |       1e-06    |   0.749293 |
| solution-2         |     0.531335 |       0.525658 |   0.911576 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.536262 |       0.11243  |   0.316641 |
| solution-aron-mark |     0.539204 |       0.111344 |   0.320255 |
| solution-flask     |     0.527758 |       1.00887  |   0.485146 |
| solution-1-flask   |     0.535285 |       1.00904  |   0.796535 |
| solution-2         |     0.538396 |       0.474226 |   4.22721  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.531454 |       0.123255 |    1.08067 |
| solution-pl        |     0.532072 |       0.11667  |    1.08623 |
| solution-flask     |     0.532266 |       1.009    |    2.19454 |
| solution-1-flask   |     0.538403 |       1.00909  |    5.94169 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.540844 |       0.144576 |    4.63384 |
| solution-aron-mark |     0.548529 |       0.148219 |    4.86186 |
| solution-flask     |     0.532179 |       1.00909  |    8.87671 |