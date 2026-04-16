# 2026-04-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.37519  |       1.04243  |   0.101626 |
| solution-aron-mark |     4.42572  |       0.149719 |   0.232322 |
| solution-pl        |     0.43178  |       0.150251 |   0.235392 |
| solution-1-flask   |     0.431762 |       1.00846  |   0.269133 |
| solution-1         |     7.47734  |       1e-06    |   0.685449 |
| solution-2         |     0.430253 |       0.677178 |   1.08445  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420591 |       0.149834 |   0.349966 |
| solution-aron-mark |     0.460588 |       0.15914  |   0.357025 |
| solution-flask     |     0.430615 |       1.00859  |   0.377447 |
| solution-1-flask   |     0.435092 |       1.00896  |   0.793548 |
| solution-2         |     0.410878 |       0.545156 |   8.1331   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434676 |       0.156196 |    1.05299 |
| solution-aron-mark |     0.421896 |       0.160026 |    1.07399 |
| solution-flask     |     0.432892 |       1.00911  |    1.57223 |
| solution-1-flask   |     0.436015 |       1.00861  |    5.8146  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.418777 |       0.182262 |    3.83308 |
| solution-pl        |     0.433029 |       0.180595 |    3.94798 |
| solution-flask     |     0.416545 |       1.00824  |    5.09563 |