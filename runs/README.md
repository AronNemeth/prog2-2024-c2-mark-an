# 2024-10-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.237    |       1.06707  |   0.084965 |
| solution-pl        |     0.559192 |       0.101579 |   0.177294 |
| solution-aron-mark |     1.85072  |       0.100964 |   0.177831 |
| solution-1-flask   |     0.574137 |       1.0081   |   0.265104 |
| solution-1         |     7.76729  |       1e-06    |   0.596428 |
| solution-2         |     4.44409  |       0.504866 |   0.937357 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.57653  |        1.00808 |   0.210416 |
| solution-aron-mark |     0.567026 |        0.10332 |   0.310892 |
| solution-pl        |     0.566469 |        0.10397 |   0.3122   |
| solution-1-flask   |     0.570205 |        1.00811 |   0.785555 |
| solution-2         |     0.564042 |        0.51422 |   2.84916  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.57136  |       1.0083   |   0.952984 |
| solution-pl        |     0.565642 |       0.109798 |   1.04236  |
| solution-aron-mark |     0.567679 |       0.110179 |   1.04492  |
| solution-1-flask   |     0.570031 |       1.00847  |   5.50449  |
| solution-2         |     0.567174 |       0.542359 |  30.5177   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.565784 |       1.00837  |    4.26224 |
| solution-pl        |     0.572419 |       0.142833 |    4.42758 |
| solution-aron-mark |     0.567849 |       0.140369 |    4.54267 |