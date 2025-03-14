# 2025-03-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.509135 |       1.0088   |   0.080445 |
| solution-aron-mark |     1.8856   |       0.152272 |   0.210522 |
| solution-pl        |     0.50619  |       0.141233 |   0.214127 |
| solution-1-flask   |     5.21984  |       1.12278  |   0.266911 |
| solution-1         |     7.54889  |       1e-06    |   0.599522 |
| solution-2         |     0.526672 |       0.535003 |   0.75657  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.509839 |       1.00872  |   0.290811 |
| solution-aron-mark |     0.504266 |       0.142386 |   0.309163 |
| solution-pl        |     0.512728 |       0.143439 |   0.310155 |
| solution-1-flask   |     0.515425 |       1.00893  |   0.806258 |
| solution-2         |     0.5083   |       0.507004 |   4.92323  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.512301 |       0.15023  |   0.907202 |
| solution-pl        |     0.509899 |       0.151345 |   0.910127 |
| solution-flask     |     0.5303   |       1.0092   |   1.2389   |
| solution-1-flask   |     0.51502  |       1.00897  |   5.73278  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.507496 |       0.180124 |    2.82551 |
| solution-pl        |     0.50853  |       0.18681  |    2.83101 |
| solution-flask     |     0.507881 |       1.00856  |    4.20296 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.522096 |       0.288215 |    17.0158 |
| solution-aron-mark |     0.510295 |       0.282219 |    17.537  |