# 2026-06-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.20139  |       1.07722  |   0.110705 |
| solution-aron-mark |     0.435248 |       0.149979 |   0.237033 |
| solution-pl        |     0.428909 |       0.155097 |   0.237238 |
| solution-1-flask   |     0.438178 |       1.00833  |   0.268076 |
| solution-1         |     7.76712  |       1e-06    |   0.66012  |
| solution-2         |     5.18008  |       0.654933 |   1.26513  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430615 |       0.152102 |   0.362475 |
| solution-aron-mark |     0.430947 |       0.152064 |   0.364342 |
| solution-flask     |     0.430646 |       1.00839  |   0.395074 |
| solution-1-flask   |     0.437873 |       1.00852  |   0.800391 |
| solution-2         |     0.431188 |       0.507618 |  24.2077   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.436393 |       0.158505 |    1.10982 |
| solution-pl        |     0.434741 |       0.156004 |    1.11155 |
| solution-flask     |     0.429852 |       1.00842  |    1.67993 |
| solution-1-flask   |     0.433821 |       1.00853  |    5.60793 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428182 |       0.181628 |    3.96497 |
| solution-aron-mark |     0.425844 |       0.182335 |    3.97529 |
| solution-flask     |     0.432868 |       1.00844  |    5.37883 |