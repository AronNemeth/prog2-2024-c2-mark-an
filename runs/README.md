# 2026-01-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.1741   |        1.0513  |   0.100265 |
| solution-aron-mark |     0.461707 |        0.15871 |   0.239399 |
| solution-pl        |     0.464453 |        0.16205 |   0.243422 |
| solution-1-flask   |     0.464609 |        1.0081  |   0.25779  |
| solution-1         |     8.81685  |        1e-06   |   0.681873 |
| solution-2         |     5.61903  |        0.63204 |   1.29955  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461831 |       0.161227 |   0.371059 |
| solution-aron-mark |     0.466518 |       0.161447 |   0.374206 |
| solution-flask     |     0.465881 |       1.00831  |   0.381354 |
| solution-1-flask   |     0.48614  |       1.00802  |   0.804762 |
| solution-2         |     0.466377 |       0.500518 |   2.77725  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.462929 |       0.166362 |    1.07887 |
| solution-aron-mark |     0.49523  |       0.171691 |    1.16995 |
| solution-flask     |     0.490146 |       1.00863  |    1.71982 |
| solution-1-flask   |     0.47764  |       1.0082   |    5.58629 |
| solution-2         |     0.460961 |       0.552771 |   28.8551  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.464588 |       0.192368 |    3.47819 |
| solution-pl        |     0.463943 |       0.190928 |    3.51167 |
| solution-flask     |     0.464345 |       1.0085   |    5.06585 |