# 2025-03-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.528706 |       1.00897  |   0.081064 |
| solution-pl        |     0.533663 |       0.145549 |   0.206945 |
| solution-aron-mark |     1.77703  |       0.147491 |   0.207374 |
| solution-1-flask   |     4.87974  |       1.06496  |   0.268726 |
| solution-1         |     7.23231  |       1e-06    |   0.599405 |
| solution-2         |     0.530177 |       0.5324   |   0.897351 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.534077 |       1.00889  |   0.290723 |
| solution-pl        |     0.53402  |       0.141492 |   0.306081 |
| solution-aron-mark |     0.530885 |       0.143577 |   0.307471 |
| solution-1-flask   |     0.537795 |       1.0089   |   0.820133 |
| solution-2         |     0.529343 |       0.501448 |   4.73417  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533322 |       0.149215 |   0.909479 |
| solution-pl        |     0.52984  |       0.150777 |   0.914454 |
| solution-flask     |     0.530005 |       1.00906  |   1.22713  |
| solution-1-flask   |     0.557102 |       1.00933  |   5.69037  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.53353  |       0.180474 |    2.81922 |
| solution-pl        |     0.531134 |       0.18508  |    2.81954 |
| solution-flask     |     0.531538 |       1.009    |    4.22811 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.542795 |       0.282332 |    17.0417 |
| solution-aron-mark |     0.530711 |       0.281253 |    17.2235 |