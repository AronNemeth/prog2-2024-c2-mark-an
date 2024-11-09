# 2024-11-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.43006  |       1.05078  |   0.111213 |
| solution-pl        |     6.10567  |       0.114316 |   0.181934 |
| solution-aron-mark |     0.589016 |       0.110795 |   0.185948 |
| solution-1-flask   |     0.612483 |       1.00956  |   0.264478 |
| solution-1         |     8.63949  |       1e-06    |   0.758085 |
| solution-2         |     0.59026  |       0.644857 |   1.05631  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.606966 |       0.11362  |   0.303117 |
| solution-pl        |     0.58842  |       0.114622 |   0.312868 |
| solution-flask     |     0.603407 |       1.00974  |   0.498724 |
| solution-1-flask   |     0.628899 |       1.00934  |   0.779128 |
| solution-2         |     0.588502 |       0.507226 |  13.1415   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.601677 |       0.140897 |    1.01096 |
| solution-aron-mark |     0.584328 |       0.120737 |    1.01701 |
| solution-flask     |     0.598658 |       1.00949  |    2.15699 |
| solution-1-flask   |     0.602372 |       1.00937  |    5.40001 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.585684 |       0.155674 |    4.73865 |
| solution-pl        |     0.587459 |       0.151586 |    4.74652 |
| solution-flask     |     0.579185 |       1.00954  |    9.04326 |