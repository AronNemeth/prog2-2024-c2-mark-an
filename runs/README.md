# 2025-12-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.75658  |       1.07072  |   0.088853 |
| solution-aron-mark |     0.426605 |       0.146118 |   0.216609 |
| solution-pl        |     0.421617 |       0.148924 |   0.221766 |
| solution-1-flask   |     0.422354 |       1.00654  |   0.235043 |
| solution-1         |     7.62067  |       1e-06    |   0.618699 |
| solution-2         |     5.02328  |       0.598159 |   1.49055  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425446 |       0.148738 |   0.331405 |
| solution-aron-mark |     0.431185 |       0.151316 |   0.33747  |
| solution-flask     |     0.429759 |       1.00644  |   0.393902 |
| solution-1-flask   |     0.437269 |       1.00701  |   0.724063 |
| solution-2         |     0.428912 |       0.484561 |  12.626    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430276 |       0.155743 |   0.990335 |
| solution-pl        |     0.420862 |       0.153066 |   0.993293 |
| solution-flask     |     0.424011 |       1.00687  |   1.70035  |
| solution-1-flask   |     0.433991 |       1.00659  |   5.36374  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42001  |       0.181216 |    4.09045 |
| solution-aron-mark |     0.420795 |       0.17917  |    4.16656 |
| solution-flask     |     0.41848  |       1.00682  |    5.45064 |