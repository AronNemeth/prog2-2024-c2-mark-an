# 2024-04-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.654392 |       1.00895  |   0.064344 |
| solution-aron-mark |     0.66905  |       0.111126 |   0.166046 |
| solution-pl        |     5.94576  |       0.112116 |   0.166269 |
| solution-1-flask   |     1.39905  |       1.04895  |   0.263888 |
| solution-1         |     7.92831  |       1e-06    |   0.591532 |
| solution-2         |     0.659337 |       0.415463 |   1.08475  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660596 |       1.00906  |   0.162298 |
| solution-pl        |     0.657236 |       0.119302 |   0.259047 |
| solution-aron-mark |     0.66597  |       0.117919 |   0.262543 |
| solution-1-flask   |     0.670935 |       1.00888  |   0.78593  |
| solution-2         |     0.664246 |       0.426158 |  11.4841   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659491 |       1.00913  |   0.719169 |
| solution-aron-mark |     0.660544 |       0.125323 |   0.826195 |
| solution-pl        |     0.661964 |       0.125523 |   0.834686 |
| solution-1-flask   |     0.672738 |       1.00872  |   5.66306  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656061 |       1.00909  |    2.48866 |
| solution-aron-mark |     0.655187 |       0.160425 |    3.35815 |
| solution-pl        |     0.653856 |       0.160088 |    3.35917 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.653474 |        1.00907 |     16.382 |