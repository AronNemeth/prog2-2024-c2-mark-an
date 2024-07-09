# 2024-07-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511508 |       1.00922  |   0.092221 |
| solution-pl        |     0.508792 |       0.103009 |   0.169347 |
| solution-aron-mark |     5.81115  |       0.103925 |   0.171801 |
| solution-1-flask   |     1.09822  |       1.095    |   0.262765 |
| solution-1         |     7.72942  |       1e-06    |   0.580253 |
| solution-2         |     0.514026 |       0.553132 |   1.71898  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.523301 |       1.00881  |   0.196317 |
| solution-pl        |     0.504214 |       0.104316 |   0.288958 |
| solution-aron-mark |     0.512713 |       0.105905 |   0.294139 |
| solution-1-flask   |     0.503999 |       1.00877  |   0.773987 |
| solution-2         |     0.50998  |       0.474811 |   2.82336  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.50539  |       1.00915  |    0.89819 |
| solution-aron-mark |     0.503479 |       0.113066 |    1.0049  |
| solution-pl        |     0.504221 |       0.112261 |    1.00863 |
| solution-1-flask   |     0.513492 |       1.00942  |    5.57735 |
| solution-2         |     0.505713 |       0.530691 |   32.8103  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500832 |       1.00915  |    4.23488 |
| solution-pl        |     0.504944 |       0.149722 |    4.28488 |
| solution-aron-mark |     0.505524 |       0.152484 |    4.29942 |