# 2026-05-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.09539  |       1.06933  |   0.109823 |
| solution-aron-mark |     5.75897  |       0.173965 |   0.236071 |
| solution-pl        |     0.431268 |       0.146858 |   0.236582 |
| solution-1-flask   |     0.433733 |       1.00801  |   0.259897 |
| solution-1         |     7.42919  |       2e-06    |   0.76696  |
| solution-2         |     0.426965 |       0.798048 |   1.80275  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.437418 |       0.154953 |   0.379991 |
| solution-aron-mark |     0.430259 |       0.150723 |   0.386337 |
| solution-flask     |     0.429614 |       1.00824  |   0.424746 |
| solution-1-flask   |     0.438053 |       1.00833  |   0.810631 |
| solution-2         |     0.42657  |       0.507078 |   2.11713  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431882 |       0.153818 |    1.16684 |
| solution-pl        |     0.431633 |       0.154097 |    1.18812 |
| solution-flask     |     0.428187 |       1.00835  |    1.72465 |
| solution-1-flask   |     0.437106 |       1.00876  |    5.71685 |
| solution-2         |     0.428602 |       0.559915 |  173.571   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432544 |       0.178144 |    4.01971 |
| solution-aron-mark |     0.424226 |       0.178271 |    4.06265 |
| solution-flask     |     0.425702 |       1.0087   |    5.54911 |