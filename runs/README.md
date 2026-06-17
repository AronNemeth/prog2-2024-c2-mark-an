# 2026-06-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2891   |       1.04658  |   0.113322 |
| solution-aron-mark |     0.45241  |       0.156549 |   0.245188 |
| solution-pl        |     6.72808  |       0.192699 |   0.250204 |
| solution-1-flask   |     0.479367 |       1.00879  |   0.274154 |
| solution-1         |     8.41624  |       1e-06    |   0.764798 |
| solution-2         |     0.455736 |       0.76476  |   1.02797  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.450959 |       0.163345 |   0.382686 |
| solution-aron-mark |     0.463837 |       0.159195 |   0.385159 |
| solution-flask     |     0.454203 |       1.00875  |   0.404166 |
| solution-1-flask   |     0.474571 |       1.00859  |   0.816204 |
| solution-2         |     0.462765 |       0.553836 |   7.3384   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.462565 |       0.168719 |    1.14384 |
| solution-pl        |     0.464441 |       0.166655 |    1.14427 |
| solution-flask     |     0.465979 |       1.00894  |    1.71837 |
| solution-1-flask   |     0.477736 |       1.00893  |    5.77929 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465094 |       0.193985 |    4.1781  |
| solution-pl        |     0.465516 |       0.192374 |    4.21066 |
| solution-flask     |     0.467019 |       1.00909  |    5.6822  |