# 2025-07-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67716  |       1.06001  |   0.101133 |
| solution-aron-mark |     4.60315  |       0.151673 |   0.238533 |
| solution-pl        |     0.510416 |       0.153192 |   0.242663 |
| solution-1-flask   |     0.519413 |       1.00861  |   0.270579 |
| solution-1         |     7.81474  |       1e-06    |   0.606019 |
| solution-2         |     0.49634  |       0.614899 |   1.42236  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512717 |       0.155644 |   0.373734 |
| solution-flask     |     0.506918 |       1.00849  |   0.384174 |
| solution-aron-mark |     0.510982 |       0.151743 |   0.385307 |
| solution-1-flask   |     0.513418 |       1.00863  |   0.805983 |
| solution-2         |     0.526382 |       0.518633 |   2.82724  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498001 |       0.162306 |    1.08316 |
| solution-aron-mark |     0.507535 |       0.161382 |    1.08884 |
| solution-flask     |     0.513829 |       1.00858  |    1.63175 |
| solution-1-flask   |     0.538826 |       1.00872  |    5.75624 |
| solution-2         |     0.494445 |       0.551447 |   24.9043  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.51026  |       0.192369 |    3.28248 |
| solution-pl        |     0.503035 |       0.191777 |    3.28871 |
| solution-flask     |     0.517853 |       1.00876  |    5.23649 |