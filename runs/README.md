# 2024-12-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85668  |       1.00903  |   0.107521 |
| solution-aron-mark |     0.532699 |       0.106863 |   0.183706 |
| solution-pl        |     0.532682 |       0.108344 |   0.186711 |
| solution-1-flask   |     5.22363  |       1.07121  |   0.267648 |
| solution-1         |     7.60208  |       1e-06    |   0.593705 |
| solution-2         |     0.529601 |       0.488762 |   0.914987 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.54107  |       0.109281 |   0.317185 |
| solution-aron-mark |     0.531373 |       0.11059  |   0.318967 |
| solution-flask     |     0.531024 |       1.00874  |   0.505458 |
| solution-1-flask   |     0.537432 |       1.0089   |   0.813622 |
| solution-2         |     0.530598 |       0.474206 |   2.81928  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.534106 |       0.116024 |    1.07121 |
| solution-aron-mark |     0.535873 |       0.115956 |    1.0867  |
| solution-flask     |     0.531414 |       1.00873  |    2.2703  |
| solution-1-flask   |     0.54012  |       1.0096   |    5.85965 |
| solution-2         |     0.541605 |       0.528704 |  177.923   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.536888 |       0.142782 |    4.37902 |
| solution-aron-mark |     0.544929 |       0.145107 |    4.41976 |
| solution-flask     |     0.531058 |       1.00879  |    8.81452 |