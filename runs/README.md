# 2025-11-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.80061  |       1.04382  |   0.103536 |
| solution-aron-mark |     0.475311 |       0.159868 |   0.243881 |
| solution-pl        |     0.479843 |       0.162527 |   0.248345 |
| solution-1-flask   |     0.497463 |       1.0084   |   0.270815 |
| solution-1         |     8.40558  |       1e-06    |   0.790724 |
| solution-2         |     5.32271  |       0.706776 |   1.27867  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.479649 |       0.162416 |   0.374632 |
| solution-aron-mark |     0.482212 |       0.160661 |   0.377707 |
| solution-flask     |     0.476842 |       1.00869  |   0.380188 |
| solution-1-flask   |     0.479974 |       1.00839  |   0.808106 |
| solution-2         |     0.476108 |       0.51355  |   6.30383  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49772  |       0.170866 |    1.10061 |
| solution-aron-mark |     0.47466  |       0.165314 |    1.10548 |
| solution-flask     |     0.482589 |       1.00882  |    1.58288 |
| solution-1-flask   |     0.482844 |       1.00839  |    5.67112 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478257 |       0.199164 |    3.31593 |
| solution-aron-mark |     0.477723 |       0.196888 |    3.35784 |
| solution-flask     |     0.498892 |       1.00854  |    5.23126 |