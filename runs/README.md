# 2026-05-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06403  |       1.08403  |   0.106704 |
| solution-1-flask   |     0.438454 |       1.00885  |   0.229072 |
| solution-pl        |     0.439376 |       0.148604 |   0.229137 |
| solution-aron-mark |     6.08427  |       0.161762 |   0.233205 |
| solution-1         |     7.52438  |       1e-06    |   0.620977 |
| solution-2         |     0.431576 |       0.71498  |   1.02215  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426711 |       0.148927 |   0.351847 |
| solution-aron-mark |     0.428274 |       0.156444 |   0.373979 |
| solution-flask     |     0.429668 |       1.00883  |   0.406468 |
| solution-1-flask   |     0.43044  |       1.0088   |   0.717639 |
| solution-2         |     0.428837 |       0.506015 |   2.50989  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432454 |       0.156508 |    1.05084 |
| solution-aron-mark |     0.42741  |       0.15439  |    1.0609  |
| solution-flask     |     0.426841 |       1.00906  |    1.69137 |
| solution-1-flask   |     0.429725 |       1.009    |    5.5391  |
| solution-2         |     0.424129 |       0.558392 |   34.9134  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427649 |       0.180657 |    3.74615 |
| solution-aron-mark |     0.427799 |       0.181095 |    3.80108 |
| solution-flask     |     0.424076 |       1.0091   |    5.32581 |