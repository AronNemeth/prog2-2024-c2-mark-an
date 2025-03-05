# 2025-03-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55505  |       1.00892  |   0.080112 |
| solution-aron-mark |     2.31978  |       0.330112 |   0.208274 |
| solution-pl        |     0.55591  |       0.146452 |   0.209807 |
| solution-1-flask   |     5.4573   |       1.11073  |   0.260459 |
| solution-1         |     8.09494  |       1e-06    |   1.02661  |
| solution-2         |     0.610964 |       0.788355 |   1.46491  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56092  |       1.00918  |   0.297211 |
| solution-pl        |     0.564757 |       0.147735 |   0.310769 |
| solution-aron-mark |     0.54972  |       0.152815 |   0.317981 |
| solution-1-flask   |     0.566978 |       1.00898  |   0.803608 |
| solution-2         |     0.55962  |       0.52417  |  13.6993   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.561625 |       0.157113 |   0.914016 |
| solution-pl        |     0.572127 |       0.155807 |   0.922343 |
| solution-flask     |     0.558377 |       1.00892  |   1.24302  |
| solution-1-flask   |     0.548586 |       1.00942  |   5.69663  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.564504 |       0.186592 |    2.91172 |
| solution-aron-mark |     0.561028 |       0.185173 |    2.94145 |
| solution-flask     |     0.558594 |       1.00913  |    4.34956 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553853 |       0.284698 |    18.3103 |
| solution-aron-mark |     0.558939 |       0.29023  |    18.4036 |