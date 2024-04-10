# 2024-04-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659809 |       1.00894  |   0.063524 |
| solution-aron-mark |     0.65171  |       0.110339 |   0.162055 |
| solution-pl        |     5.64895  |       0.109999 |   0.163307 |
| solution-1-flask   |     1.40547  |       1.07313  |   0.261951 |
| solution-1         |     7.87825  |       2e-06    |   0.632038 |
| solution-2         |     0.645832 |       0.411143 |   1.50036  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656532 |       1.00892  |   0.176183 |
| solution-pl        |     0.669881 |       0.114474 |   0.255017 |
| solution-aron-mark |     0.654578 |       0.116118 |   0.25779  |
| solution-1-flask   |     0.670523 |       1.00927  |   0.805892 |
| solution-2         |     0.659717 |       0.423624 |   7.23741  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.669427 |       0.123133 |   0.812956 |
| solution-pl        |     0.655932 |       0.122597 |   0.821935 |
| solution-flask     |     0.67411  |       1.00899  |   0.91947  |
| solution-1-flask   |     0.674241 |       1.0092   |   5.60275  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.66031  |       0.158943 |    3.21053 |
| solution-aron-mark |     0.660449 |       0.158036 |    3.2449  |
| solution-flask     |     0.661537 |       1.00929  |    5.25812 |