# 2025-08-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.17236  |       2.14288  |   0.102276 |
| solution-pl        |     0.945763 |       0.154851 |   0.239039 |
| solution-aron-mark |     5.14305  |       0.151642 |   0.24133  |
| solution-1-flask   |     0.96334  |       1.00864  |   0.266282 |
| solution-1         |     8.53312  |       1e-06    |   1.2514   |
| solution-2         |     0.967556 |       1.17122  |   1.36605  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.941131 |       0.155399 |   0.364037 |
| solution-aron-mark |     0.949061 |       0.153497 |   0.365489 |
| solution-flask     |     0.93665  |       1.00835  |   0.372473 |
| solution-1-flask   |     0.957981 |       1.00851  |   0.811098 |
| solution-2         |     0.938057 |       0.501781 |   7.74657  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.938752 |       0.160532 |    1.06004 |
| solution-aron-mark |     0.944479 |       0.161614 |    1.07366 |
| solution-flask     |     0.942215 |       1.00872  |    1.5656  |
| solution-1-flask   |     0.663542 |       1.00829  |    5.71819 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.488649 |       0.188912 |    3.25487 |
| solution-pl        |     0.491046 |       0.192249 |    3.28164 |
| solution-flask     |     0.48584  |       1.00831  |    5.15876 |