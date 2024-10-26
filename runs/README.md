# 2024-10-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2527   |       1.1991   |   0.108755 |
| solution-pl        |     5.7272   |       0.108689 |   0.173051 |
| solution-aron-mark |     0.546411 |       0.106204 |   0.192693 |
| solution-1-flask   |     0.554915 |       1.00919  |   0.253641 |
| solution-1         |     7.56199  |       1e-06    |   0.579471 |
| solution-2         |     0.552732 |       0.485364 |   1.20697  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553156 |       0.107666 |   0.30119  |
| solution-aron-mark |     0.55495  |       0.109094 |   0.302133 |
| solution-flask     |     0.550427 |       1.00879  |   0.497354 |
| solution-1-flask   |     0.555776 |       1.00882  |   0.762612 |
| solution-2         |     0.550192 |       0.526242 |   3.4492   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549862 |       0.116918 |    1.00462 |
| solution-aron-mark |     0.585778 |       0.117562 |    1.01109 |
| solution-flask     |     0.550976 |       1.00897  |    2.13229 |
| solution-1-flask   |     0.561012 |       1.0091   |    5.32812 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.549989 |       0.14556  |    4.15181 |
| solution-aron-mark |     0.550876 |       0.146482 |    4.17111 |
| solution-flask     |     0.55214  |       1.00894  |    8.26678 |