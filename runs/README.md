# 2026-05-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.01563  |       1.09456  |   0.106112 |
| solution-1-flask   |     0.434847 |       1.0086   |   0.22932  |
| solution-pl        |     0.42983  |       0.151249 |   0.233046 |
| solution-aron-mark |     6.30649  |       0.166629 |   0.233803 |
| solution-1         |     7.34011  |       1e-06    |   0.610488 |
| solution-2         |     0.431197 |       0.717218 |   0.88903  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.43031  |       0.152916 |   0.357771 |
| solution-pl        |     0.42668  |       0.152528 |   0.360784 |
| solution-flask     |     0.4345   |       1.00899  |   0.407487 |
| solution-1-flask   |     0.444284 |       1.00866  |   0.719122 |
| solution-2         |     0.433017 |       0.509552 |   1.95233  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.428488 |       0.160849 |    1.05661 |
| solution-pl        |     0.422603 |       0.159785 |    1.06652 |
| solution-flask     |     0.433989 |       1.00866  |    1.68133 |
| solution-1-flask   |     0.434345 |       1.00872  |    5.55391 |
| solution-2         |     0.434896 |       0.561653 |   38.4016  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424424 |       0.183328 |    3.74472 |
| solution-pl        |     0.424591 |       0.182989 |    3.78283 |
| solution-flask     |     0.423717 |       1.00872  |    5.34672 |