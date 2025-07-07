# 2025-07-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0707   |       1.06807  |   0.102469 |
| solution-pl        |     0.493372 |       0.149265 |   0.236441 |
| solution-aron-mark |     5.50173  |       0.238728 |   0.245251 |
| solution-1-flask   |     0.511916 |       1.00845  |   0.267859 |
| solution-1         |     7.59121  |       1e-06    |   0.696635 |
| solution-2         |     0.500148 |       0.688665 |   0.852767 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.548361 |       0.150625 |   0.364407 |
| solution-pl        |     0.498617 |       0.153777 |   0.365575 |
| solution-flask     |     0.496872 |       1.0086   |   0.388576 |
| solution-1-flask   |     0.507091 |       1.00927  |   0.801058 |
| solution-2         |     0.496227 |       0.498935 |   7.19601  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501686 |       0.1604   |    1.08199 |
| solution-aron-mark |     0.497761 |       0.160589 |    1.08347 |
| solution-flask     |     0.499373 |       1.00876  |    1.60595 |
| solution-1-flask   |     0.509909 |       1.00918  |    5.73048 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496208 |       0.191735 |    3.28141 |
| solution-pl        |     0.497328 |       0.19311  |    3.30919 |
| solution-flask     |     0.50758  |       1.00889  |    5.11645 |