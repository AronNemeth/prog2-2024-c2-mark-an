# 2025-10-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.79892  |       1.03711  |   0.101055 |
| solution-pl        |     0.505268 |       0.159487 |   0.24254  |
| solution-aron-mark |     0.503049 |       0.159213 |   0.244915 |
| solution-1-flask   |     0.51048  |       1.00821  |   0.268006 |
| solution-1         |    13.5088   |       1e-06    |   0.707901 |
| solution-2         |     4.91111  |       0.696831 |   1.20822  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50424  |       0.165203 |   0.370792 |
| solution-aron-mark |     0.515104 |       0.166293 |   0.375886 |
| solution-flask     |     0.507654 |       1.00854  |   0.379621 |
| solution-1-flask   |     0.51748  |       1.00869  |   0.79868  |
| solution-2         |     0.499369 |       0.53282  |   6.84471  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.516774 |       0.176061 |    1.08203 |
| solution-pl        |     0.527603 |       0.17276  |    1.08326 |
| solution-flask     |     0.508635 |       1.00861  |    1.59922 |
| solution-1-flask   |     0.506944 |       1.00884  |    5.77226 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.507564 |       0.203954 |    3.373   |
| solution-aron-mark |     0.509372 |       0.20518  |    3.37924 |
| solution-flask     |     0.506393 |       1.00875  |    5.3204  |