# 2026-03-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.74523  |       1.05186  |   0.105295 |
| solution-1-flask   |     0.481613 |       1.00959  |   0.230519 |
| solution-aron-mark |     0.472917 |       0.157392 |   0.23989  |
| solution-pl        |     4.98912  |       0.158139 |   0.241578 |
| solution-1         |     8.46593  |       1e-06    |   0.708917 |
| solution-2         |     0.478003 |       0.687215 |   1.078    |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473423 |       0.159036 |   0.364997 |
| solution-aron-mark |     0.477011 |       0.161143 |   0.369556 |
| solution-flask     |     0.476439 |       1.01026  |   0.401125 |
| solution-1-flask   |     0.478733 |       1.00972  |   0.725986 |
| solution-2         |     0.472617 |       0.552579 |   3.80273  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475437 |       0.167717 |    1.07642 |
| solution-pl        |     0.47377  |       0.164249 |    1.0771  |
| solution-flask     |     0.476393 |       1.00985  |    1.69269 |
| solution-1-flask   |     0.478703 |       1.00979  |    5.62319 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.471957 |       0.193679 |    4.22552 |
| solution-aron-mark |     0.474927 |       0.192572 |    4.22875 |
| solution-flask     |     0.474298 |       1.01106  |    5.4999  |