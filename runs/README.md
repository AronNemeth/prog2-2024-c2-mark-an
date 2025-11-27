# 2025-11-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.33662  |       1.06221  |   0.101302 |
| solution-aron-mark |     0.463381 |       0.155161 |   0.241335 |
| solution-pl        |     0.467153 |       0.155993 |   0.242089 |
| solution-1-flask   |     0.479947 |       1.00823  |   0.264897 |
| solution-1         |     8.40255  |       1e-06    |   0.700632 |
| solution-2         |     4.73146  |       0.673592 |   0.817464 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469115 |       0.158881 |   0.370605 |
| solution-aron-mark |     0.46588  |       0.159601 |   0.374293 |
| solution-flask     |     0.469375 |       1.00829  |   0.37742  |
| solution-1-flask   |     0.471152 |       1.00835  |   0.783819 |
| solution-2         |     0.466681 |       0.50601  |   3.30804  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468049 |       0.164595 |    1.0852  |
| solution-pl        |     0.467931 |       0.165487 |    1.09644 |
| solution-flask     |     0.472218 |       1.00835  |    1.57625 |
| solution-1-flask   |     0.474702 |       1.0088   |    5.5582  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462682 |       0.195987 |    3.23364 |
| solution-aron-mark |     0.468565 |       0.196523 |    3.23832 |
| solution-flask     |     0.469413 |       1.0085   |    5.0659  |