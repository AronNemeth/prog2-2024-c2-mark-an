# 2026-09-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2064   |       1.0622   |   0.105459 |
| solution-1-flask   |     0.42442  |       1.00897  |   0.226245 |
| solution-aron-mark |     0.415513 |       0.151538 |   0.229685 |
| solution-pl        |     2.42116  |       0.154003 |   0.230249 |
| solution-1         |     7.74182  |       1e-06    |   0.544595 |
| solution-2         |     4.76417  |       0.523144 |   0.993387 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.421832 |       0.153932 |   0.353194 |
| solution-pl        |     0.42555  |       0.157355 |   0.375143 |
| solution-flask     |     0.421643 |       1.00893  |   0.38642  |
| solution-1-flask   |     0.426282 |       1.00891  |   0.740397 |
| solution-2         |     0.41711  |       0.493871 |  10.9341   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.427975 |       0.160342 |    1.03072 |
| solution-aron-mark |     0.418015 |       0.16054  |    1.03131 |
| solution-flask     |     0.416877 |       1.00883  |    1.62268 |
| solution-1-flask   |     0.423097 |       1.00894  |    5.61038 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422316 |       0.182278 |    3.42804 |
| solution-pl        |     0.421601 |       0.184669 |    3.4313  |
| solution-flask     |     0.418564 |       1.00897  |    5.09825 |