# 2024-10-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08653  |       1.12146  |   0.083692 |
| solution-pl        |     0.560182 |       0.102131 |   0.177592 |
| solution-aron-mark |     1.78505  |       0.104326 |   0.178653 |
| solution-1-flask   |     0.570472 |       1.00782  |   0.26744  |
| solution-1         |     7.54206  |       1e-06    |   0.59851  |
| solution-2         |     4.38204  |       0.571971 |   1.25286  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56324  |       1.00858  |   0.21264  |
| solution-pl        |     0.563124 |       0.105173 |   0.310332 |
| solution-aron-mark |     0.57145  |       0.108692 |   0.323415 |
| solution-1-flask   |     0.56916  |       1.00802  |   0.77307  |
| solution-2         |     0.552909 |       0.480449 |   2.49093  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.562344 |       1.0081   |   0.957285 |
| solution-aron-mark |     0.566741 |       0.115391 |   1.06495  |
| solution-pl        |     0.561261 |       0.111359 |   1.06531  |
| solution-1-flask   |     0.559187 |       1.00832  |   5.47305  |
| solution-2         |     0.567126 |       0.537011 | 162.794    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550135 |       1.00796  |    4.12554 |
| solution-aron-mark |     0.554111 |       0.137486 |    4.38534 |
| solution-pl        |     0.562553 |       0.139257 |    4.41215 |