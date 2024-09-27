# 2024-09-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27257  |       1.05992  |   0.09608  |
| solution-pl        |     0.560486 |       0.103814 |   0.180002 |
| solution-aron-mark |     2.53999  |       0.102071 |   0.180236 |
| solution-1-flask   |     0.566007 |       1.00803  |   0.269652 |
| solution-1         |     8.80727  |       1e-06    |   0.634131 |
| solution-2         |     4.52407  |       0.494557 |   1.23364  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551957 |       1.0087   |   0.209506 |
| solution-aron-mark |     0.556544 |       0.103017 |   0.308948 |
| solution-pl        |     0.56297  |       0.105931 |   0.316523 |
| solution-1-flask   |     0.563497 |       1.00829  |   0.791117 |
| solution-2         |     0.554531 |       0.477277 |   2.16578  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561634 |       1.00839  |   0.967857 |
| solution-aron-mark |     0.573269 |       0.109783 |   1.04288  |
| solution-pl        |     0.555992 |       0.109989 |   1.05665  |
| solution-1-flask   |     0.562291 |       1.00826  |   5.47875  |
| solution-2         |     0.565471 |       0.525967 | 314.119    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552013 |       1.00826  |    4.06818 |
| solution-aron-mark |     0.555169 |       0.141944 |    4.15831 |
| solution-pl        |     0.553506 |       0.137344 |    4.19809 |