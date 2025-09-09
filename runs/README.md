# 2025-09-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.473936 |       1.0081   |   0.101752 |
| solution-aron-mark |     0.466901 |       0.145552 |   0.232166 |
| solution-pl        |     5.60346  |       0.152939 |   0.236112 |
| solution-1-flask   |     1.13889  |       1.04323  |   0.261713 |
| solution-1         |     7.56967  |       1e-06    |   0.579138 |
| solution-2         |     0.473981 |       0.608402 |   0.809639 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473289 |       0.151013 |   0.361097 |
| solution-pl        |     0.47418  |       0.151955 |   0.361339 |
| solution-flask     |     0.491445 |       1.00824  |   0.374013 |
| solution-1-flask   |     0.474135 |       1.0082   |   0.788224 |
| solution-2         |     0.472282 |       0.496906 |   3.5089   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.470727 |       0.158695 |    1.04676 |
| solution-aron-mark |     0.471115 |       0.157143 |    1.09597 |
| solution-flask     |     0.47409  |       1.00802  |    1.59191 |
| solution-1-flask   |     0.4709   |       1.00981  |    5.47877 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.466651 |       0.189973 |    3.2036  |
| solution-pl        |     0.46613  |       0.189133 |    3.22367 |
| solution-flask     |     0.470535 |       1.00826  |    5.04221 |