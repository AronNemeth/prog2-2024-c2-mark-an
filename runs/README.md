# 2024-07-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.18513  |       1.05879  |   0.097301 |
| solution-aron-mark |     0.504896 |       0.103216 |   0.166    |
| solution-pl        |     5.85142  |       0.104726 |   0.167963 |
| solution-1-flask   |     0.509419 |       1.00878  |   0.262934 |
| solution-1         |     7.89458  |       1e-06    |   0.738792 |
| solution-2         |     0.494576 |       0.63498  |   0.874846 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.495308 |       1.00901  |   0.221908 |
| solution-aron-mark |     0.500359 |       0.103602 |   0.285037 |
| solution-pl        |     0.496984 |       0.104838 |   0.28819  |
| solution-1-flask   |     0.498015 |       1.00888  |   0.787296 |
| solution-2         |     0.506306 |       0.470046 |   2.41891  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492962 |       1.00895  |   0.885152 |
| solution-pl        |     0.506699 |       0.111236 |   0.979393 |
| solution-aron-mark |     0.519497 |       0.111848 |   0.986043 |
| solution-1-flask   |     0.510012 |       1.00895  |   5.6149   |
| solution-2         |     0.497848 |       0.524592 | 169.194    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492635 |       1.00947  |    4.05464 |
| solution-pl        |     0.500047 |       0.147011 |    4.11405 |
| solution-aron-mark |     0.500288 |       0.144751 |    4.20625 |