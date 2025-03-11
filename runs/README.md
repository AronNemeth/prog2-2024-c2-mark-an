# 2025-03-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.535655 |       1.0087   |   0.080855 |
| solution-aron-mark |     1.72794  |       0.151162 |   0.20601  |
| solution-pl        |     0.533255 |       0.144168 |   0.221308 |
| solution-1-flask   |     4.91129  |       1.08365  |   0.259399 |
| solution-1         |     7.2374   |       1e-06    |   0.590369 |
| solution-2         |     0.529856 |       0.576173 |   1.21258  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.533691 |       1.00881  |   0.28619  |
| solution-pl        |     0.531411 |       0.142308 |   0.307543 |
| solution-aron-mark |     0.528512 |       0.143547 |   0.308161 |
| solution-1-flask   |     0.536694 |       1.0089   |   0.778214 |
| solution-2         |     0.541016 |       0.503213 |  15.829    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.535739 |       0.149971 |   0.908778 |
| solution-pl        |     0.532164 |       0.152245 |   0.916007 |
| solution-flask     |     0.526829 |       1.00878  |   1.222    |
| solution-1-flask   |     0.53746  |       1.00894  |   5.6397   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535059 |       0.176936 |    2.81574 |
| solution-aron-mark |     0.529011 |       0.178887 |    2.8361  |
| solution-flask     |     0.533584 |       1.00923  |    4.20628 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534525 |       0.282836 |    16.3424 |
| solution-pl        |     0.531763 |       0.276591 |    16.7639 |