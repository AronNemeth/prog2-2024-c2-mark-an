# 2025-07-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.45274  |       1.05686  |   0.100621 |
| solution-pl        |     0.508712 |       0.151595 |   0.23788  |
| solution-aron-mark |     4.77114  |       0.152733 |   0.239599 |
| solution-1-flask   |     0.519199 |       1.00825  |   0.270951 |
| solution-1         |     7.9389   |       1e-06    |   0.680923 |
| solution-2         |     0.514635 |       0.642987 |   1.21546  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506601 |       0.15258  |   0.363255 |
| solution-aron-mark |     0.502557 |       0.151734 |   0.364086 |
| solution-flask     |     0.515373 |       1.00853  |   0.379873 |
| solution-1-flask   |     0.507796 |       1.00859  |   0.814053 |
| solution-2         |     0.522396 |       0.510057 |   2.88738  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.521306 |       0.159852 |    1.06611 |
| solution-pl        |     0.506829 |       0.159455 |    1.07543 |
| solution-flask     |     0.510776 |       1.00877  |    1.58092 |
| solution-1-flask   |     0.511289 |       1.00856  |    5.66578 |
| solution-2         |     0.500899 |       0.561404 |  313.732   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.513108 |       0.191786 |    3.28069 |
| solution-pl        |     0.519946 |       0.191674 |    3.29857 |
| solution-flask     |     0.503245 |       1.00832  |    5.1008  |