# 2025-10-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.00005  |       1.15487  |   0.109934 |
| solution-pl        |     0.949356 |       0.158052 |   0.243335 |
| solution-aron-mark |     0.946574 |       0.156209 |   0.245795 |
| solution-1-flask   |     0.949333 |       1.00819  |   0.283963 |
| solution-2         |     4.96295  |       1.00181  |   1.08332  |
| solution-1         |     8.79374  |       1e-06    |   1.23013  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.948662 |       0.159944 |   0.367976 |
| solution-pl        |     0.952775 |       0.160093 |   0.368437 |
| solution-flask     |     0.943087 |       1.00866  |   0.380818 |
| solution-1-flask   |     0.949694 |       1.00857  |   0.803579 |
| solution-2         |     0.944136 |       0.513896 |  11.8803   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.858238 |       0.167378 |    1.08642 |
| solution-pl        |     0.497312 |       0.166341 |    1.09197 |
| solution-flask     |     0.944607 |       1.00847  |    1.59666 |
| solution-1-flask   |     0.498433 |       1.00866  |    5.66212 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490523 |       0.19656  |    3.29334 |
| solution-aron-mark |     0.498154 |       0.199134 |    3.31076 |
| solution-flask     |     0.49502  |       1.00883  |    5.22897 |