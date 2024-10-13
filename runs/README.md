# 2024-10-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.507672 |       1.00848  |   0.09246  |
| solution-pl        |     0.510689 |       0.103531 |   0.175554 |
| solution-aron-mark |     1.9002   |       0.101861 |   0.17591  |
| solution-1-flask   |     5.15816  |       1.08358  |   0.263244 |
| solution-1         |     7.83128  |       1e-06    |   0.631763 |
| solution-2         |     0.509139 |       0.526133 |   1.29923  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508585 |       1.00865  |   0.208933 |
| solution-aron-mark |     0.514354 |       0.104518 |   0.304296 |
| solution-pl        |     0.511919 |       0.102649 |   0.305764 |
| solution-1-flask   |     0.519057 |       1.00833  |   0.80489  |
| solution-2         |     0.512927 |       0.471678 |   6.77911  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.511728 |       1.00872  |   0.931046 |
| solution-aron-mark |     0.518038 |       0.110189 |   1.03857  |
| solution-pl        |     0.509583 |       0.109437 |   1.04396  |
| solution-1-flask   |     0.512919 |       1.01004  |   5.88949  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.509703 |       1.00921  |    4.12449 |
| solution-pl        |     0.507463 |       0.137711 |    4.25033 |
| solution-aron-mark |     0.50906  |       0.139642 |    4.26287 |