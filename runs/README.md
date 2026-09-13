# 2026-09-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.19466  |       1.04458  |   0.11502  |
| solution-aron-mark |     0.439316 |       0.160403 |   0.247049 |
| solution-pl        |     2.29203  |       0.171426 |   0.251086 |
| solution-1-flask   |     0.45246  |       1.00838  |   0.274983 |
| solution-1         |     7.56144  |       1e-06    |   0.685265 |
| solution-2         |     5.01206  |       0.642657 |   1.9382   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.444731 |       0.160614 |   0.388817 |
| solution-pl        |     0.439043 |       0.159015 |   0.38888  |
| solution-flask     |     0.445307 |       1.00871  |   0.409517 |
| solution-1-flask   |     0.451196 |       1.00863  |   0.835439 |
| solution-2         |     0.444288 |       0.532312 |   2.78601  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.441021 |       0.162649 |    1.14922 |
| solution-aron-mark |     0.459466 |       0.165414 |    1.15064 |
| solution-flask     |     0.439646 |       1.00878  |    1.71118 |
| solution-1-flask   |     0.456407 |       1.00864  |    5.92672 |
| solution-2         |     0.445622 |       0.57434  |   33.1908  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.441291 |       0.190118 |    3.6792  |
| solution-aron-mark |     0.444987 |       0.187338 |    3.70971 |
| solution-flask     |     0.447583 |       1.00927  |    5.65548 |