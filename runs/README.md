# 2025-03-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.546565 |       1.00969  |   0.084435 |
| solution-pl        |     0.533241 |       0.14556  |   0.207908 |
| solution-aron-mark |     1.84717  |       0.344897 |   0.210499 |
| solution-1-flask   |     4.94913  |       1.08944  |   0.273053 |
| solution-1         |     7.334    |       1e-06    |   1.07668  |
| solution-2         |     0.535281 |       0.747717 |   1.13022  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.564055 |       1.00961  |   0.303898 |
| solution-aron-mark |     0.5471   |       0.157079 |   0.317535 |
| solution-pl        |     0.579944 |       0.148264 |   0.323766 |
| solution-1-flask   |     0.581857 |       1.00999  |   0.802956 |
| solution-2         |     0.58064  |       0.562538 |   3.52745  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.578566 |       0.166635 |   0.930025 |
| solution-aron-mark |     0.551278 |       0.155963 |   0.932995 |
| solution-flask     |     0.621407 |       1.00998  |   1.28045  |
| solution-1-flask   |     0.542186 |       1.0092   |   5.72565  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.537562 |       0.18076  |    2.8946  |
| solution-aron-mark |     0.555617 |       0.187997 |    2.92485 |
| solution-flask     |     0.55078  |       1.01044  |    4.24641 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.601459 |       0.286786 |    21.0867 |
| solution-pl        |     0.572201 |       0.29518  |    21.8458 |