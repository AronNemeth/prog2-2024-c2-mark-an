# 2025-02-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.52776  |       1.00981  |   0.084278 |
| solution-aron-mark |     0.53584  |       0.140264 |   0.206725 |
| solution-pl        |     1.87004  |       0.153073 |   0.207451 |
| solution-1-flask   |     4.85816  |       1.0609   |   0.268891 |
| solution-1         |     7.1511   |       1e-06    |   0.6017   |
| solution-2         |     0.529418 |       0.62433  |   1.15113  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.526851 |       1.00879  |   0.289524 |
| solution-aron-mark |     0.531432 |       0.142987 |   0.307619 |
| solution-pl        |     0.52387  |       0.142637 |   0.308023 |
| solution-1-flask   |     0.53187  |       1.00868  |   0.806375 |
| solution-2         |     0.528715 |       0.49973  |   5.53357  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530828 |       0.148596 |   0.896095 |
| solution-pl        |     0.527308 |       0.149408 |   0.908739 |
| solution-flask     |     0.537344 |       1.00887  |   1.2503   |
| solution-1-flask   |     0.534803 |       1.0087   |   5.62955  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529133 |       0.176894 |    2.83401 |
| solution-aron-mark |     0.527662 |       0.173283 |    2.86601 |
| solution-flask     |     0.529497 |       1.00968  |    4.22133 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527735 |       0.27545  |    16.1897 |
| solution-pl        |     0.542285 |       0.274653 |    16.5781 |