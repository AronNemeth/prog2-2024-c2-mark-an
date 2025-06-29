# 2025-06-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.44358  |       1.0411   |   0.102532 |
| solution-pl        |     0.499232 |       0.151142 |   0.23621  |
| solution-aron-mark |     5.99083  |       0.156566 |   0.238979 |
| solution-1-flask   |     0.514634 |       1.00828  |   0.26926  |
| solution-1         |     8.00949  |       1e-06    |   0.666709 |
| solution-2         |     0.514024 |       0.591084 |   1.12881  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51115  |       0.152073 |   0.361444 |
| solution-pl        |     0.50185  |       0.152286 |   0.366346 |
| solution-flask     |     0.503937 |       1.00847  |   0.375168 |
| solution-1-flask   |     0.513606 |       1.00843  |   0.808379 |
| solution-2         |     0.511631 |       0.518563 |   5.888    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.530948 |       0.158662 |    1.07253 |
| solution-aron-mark |     0.507455 |       0.157691 |    1.07377 |
| solution-flask     |     0.506669 |       1.00859  |    1.61765 |
| solution-1-flask   |     0.513332 |       1.00839  |    5.7981  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506948 |       0.191078 |    3.25344 |
| solution-pl        |     0.506289 |       0.19376  |    3.2705  |
| solution-flask     |     0.510501 |       1.00837  |    5.16998 |