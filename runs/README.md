# 2025-11-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.08901  |       1.10821  |   0.100735 |
| solution-pl        |     0.465799 |       0.155928 |   0.242458 |
| solution-aron-mark |     0.471399 |       0.157142 |   0.252059 |
| solution-1-flask   |     0.472997 |       1.00834  |   0.265055 |
| solution-1         |     9.19348  |       1e-06    |   0.674393 |
| solution-2         |     4.91744  |       0.725191 |   1.34072  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468766 |       0.161236 |   0.370654 |
| solution-pl        |     0.466236 |       0.161792 |   0.374997 |
| solution-flask     |     0.462412 |       1.00828  |   0.384801 |
| solution-1-flask   |     0.468634 |       1.00839  |   0.800982 |
| solution-2         |     0.459613 |       0.498597 |   2.07483  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468624 |       0.166142 |    1.10135 |
| solution-pl        |     0.463625 |       0.166461 |    1.11215 |
| solution-flask     |     0.466518 |       1.00835  |    1.59352 |
| solution-1-flask   |     0.467219 |       1.00851  |    5.62383 |
| solution-2         |     0.469357 |       0.571182 |   33.5296  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468237 |       0.193554 |    3.25005 |
| solution-pl        |     0.461847 |       0.193636 |    3.25817 |
| solution-flask     |     0.46695  |       1.00833  |    5.08114 |