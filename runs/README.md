# 2026-11-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.266863 |       1.00915  |   0.043936 |
| solution-1-flask   |     0.734687 |       1.08005  |   0.128058 |
| solution-pl        |     4.87354  |       0.131468 |   0.141154 |
| solution-aron-mark |     0.269498 |       0.142868 |   0.196414 |
| solution-1         |     5.03617  |       0        |   0.335147 |
| solution-2         |     0.265111 |       0.352097 |   0.63747  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.278132 |       1.00917  |   0.09993  |
| solution-aron-mark |     0.268183 |       0.106616 |   0.198998 |
| solution-pl        |     0.272725 |       0.105048 |   0.201326 |
| solution-1-flask   |     0.269436 |       1.00926  |   0.353008 |
| solution-2         |     0.256338 |       0.346375 |   1.88057  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.266815 |       1.00951  |   0.428953 |
| solution-aron-mark |     0.26743  |       0.111381 |   0.515787 |
| solution-pl        |     0.27018  |       0.114073 |   0.536555 |
| solution-1-flask   |     0.282329 |       1.00894  |   2.69021  |
| solution-2         |     0.269238 |       0.365324 |  11.6244   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.27055  |       0.134697 |    1.84495 |
| solution-pl        |     0.26491  |       0.141761 |    1.86512 |
| solution-flask     |     0.268024 |       1.00896  |    2.21243 |
| solution-1-flask   |     0.263073 |       1.00903  |   24.17    |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.279058 |       0.203069 |    13.5439 |
| solution-aron-mark |     0.274337 |       0.236389 |    13.8212 |
| solution-flask     |     0.287556 |       1.00905  |    16.3035 |