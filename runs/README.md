# 2026-04-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.49486  |       1.05948  |   0.101388 |
| solution-pl        |     0.416609 |       0.151513 |   0.23193  |
| solution-aron-mark |     4.44914  |       0.151261 |   0.232188 |
| solution-1-flask   |     0.428078 |       1.00823  |   0.275484 |
| solution-1         |     7.75357  |       1e-06    |   0.773304 |
| solution-2         |     0.416458 |       0.568425 |   1.25874  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.41963  |       0.150836 |   0.356867 |
| solution-aron-mark |     0.420683 |       0.152323 |   0.358415 |
| solution-flask     |     0.421973 |       1.00842  |   0.374359 |
| solution-1-flask   |     0.421356 |       1.00824  |   0.790138 |
| solution-2         |     0.415434 |       0.517853 |   4.04858  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422462 |       0.156692 |    1.08632 |
| solution-aron-mark |     0.413074 |       0.154642 |    1.08779 |
| solution-flask     |     0.425407 |       1.00833  |    1.60322 |
| solution-1-flask   |     0.42983  |       1.00863  |    5.84457 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.417108 |       0.179327 |    3.93413 |
| solution-aron-mark |     0.437527 |       0.182652 |    3.99797 |
| solution-flask     |     0.420452 |       1.00895  |    5.35954 |