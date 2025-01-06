# 2025-01-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.92262  |       1.00892  |   0.107928 |
| solution-pl        |     0.576546 |       0.115341 |   0.187882 |
| solution-aron-mark |     0.57055  |       0.114962 |   0.191108 |
| solution-1-flask   |     5.88052  |       1.10118  |   0.273704 |
| solution-1         |     8.53957  |       1e-06    |   0.821727 |
| solution-2         |     0.572063 |       0.707643 |   0.950828 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.566209 |       0.122875 |   0.32227  |
| solution-pl        |     0.565269 |       0.116775 |   0.325915 |
| solution-flask     |     0.562728 |       1.00932  |   0.49108  |
| solution-1-flask   |     0.570314 |       1.00906  |   0.810665 |
| solution-2         |     0.557378 |       0.525284 |   5.36825  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.553883 |       0.131755 |    1.0867  |
| solution-pl        |     0.56911  |       0.120031 |    1.0945  |
| solution-flask     |     0.568899 |       1.00874  |    2.19451 |
| solution-1-flask   |     0.572003 |       1.00911  |    6.1006  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.571251 |       0.148655 |    4.7506  |
| solution-pl        |     0.556035 |       0.149744 |    4.91409 |
| solution-flask     |     0.572419 |       1.00936  |    9.01422 |