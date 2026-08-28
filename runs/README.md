# 2026-08-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94709  |       1.03951  |   0.111599 |
| solution-aron-mark |     5.01303  |       0.15966  |   0.255102 |
| solution-pl        |     0.456053 |       0.160762 |   0.256324 |
| solution-1-flask   |     0.451145 |       1.00825  |   0.267766 |
| solution-1         |     8.1727   |       1e-06    |   0.799263 |
| solution-2         |     0.481684 |       0.699109 |   1.42985  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462273 |       0.168249 |   0.390745 |
| solution-aron-mark |     0.468353 |       0.176306 |   0.398153 |
| solution-flask     |     0.457938 |       1.0092   |   0.404448 |
| solution-1-flask   |     0.538656 |       1.00889  |   0.820504 |
| solution-2         |     0.458743 |       0.539827 |  13.4339   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462154 |       0.172401 |    1.14853 |
| solution-aron-mark |     0.474845 |       0.176892 |    1.15212 |
| solution-flask     |     0.469098 |       1.00907  |    1.69149 |
| solution-1-flask   |     0.461628 |       1.0089   |    5.93995 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45816  |       0.19479  |    3.77605 |
| solution-pl        |     0.449837 |       0.195562 |    3.81296 |
| solution-flask     |     0.449624 |       1.00888  |    5.6045  |