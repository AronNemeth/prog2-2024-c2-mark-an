# 2025-12-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.36666  |       1.07486  |   0.098799 |
| solution-pl        |     0.468527 |       0.160998 |   0.244001 |
| solution-aron-mark |     0.478251 |       0.160425 |   0.248147 |
| solution-1-flask   |     0.476512 |       1.00831  |   0.263718 |
| solution-1         |     8.54111  |       1e-06    |   0.699723 |
| solution-2         |     4.95913  |       0.69052  |   0.906075 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475209 |       0.162395 |   0.366474 |
| solution-pl        |     0.475381 |       0.162768 |   0.369586 |
| solution-flask     |     0.466892 |       1.00854  |   0.378232 |
| solution-1-flask   |     0.474999 |       1.00817  |   0.788577 |
| solution-2         |     0.469968 |       0.506977 |   2.35616  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470856 |       0.166776 |    1.06539 |
| solution-pl        |     0.469592 |       0.166576 |    1.08113 |
| solution-flask     |     0.477593 |       1.00841  |    1.5416  |
| solution-1-flask   |     0.475217 |       1.0084   |    5.53743 |
| solution-2         |     0.470855 |       0.561674 |  163.288   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470638 |       0.19228  |    3.49231 |
| solution-pl        |     0.47508  |       0.190634 |    3.50564 |
| solution-flask     |     0.46584  |       1.00879  |    5.03294 |