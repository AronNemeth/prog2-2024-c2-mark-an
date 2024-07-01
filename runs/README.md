# 2024-07-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.523743 |       1.01003  |   0.075487 |
| solution-aron-mark |     6.28382  |       0.101884 |   0.168522 |
| solution-pl        |     0.544462 |       0.112004 |   0.175459 |
| solution-1-flask   |     1.11803  |       1.12444  |   0.260907 |
| solution-1         |     8.07263  |       1e-06    |   0.607528 |
| solution-2         |     0.510427 |       0.528961 |   0.767304 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.536955 |       1.00919  |   0.191539 |
| solution-pl        |     0.514141 |       0.106042 |   0.284612 |
| solution-aron-mark |     0.51474  |       0.10474  |   0.293039 |
| solution-1-flask   |     0.524114 |       1.009    |   0.775252 |
| solution-2         |     0.528127 |       0.493168 |   3.7807   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.516364 |       1.00904  |   0.889807 |
| solution-aron-mark |     0.514373 |       0.11052  |   0.98786  |
| solution-pl        |     0.509433 |       0.114696 |   1.00789  |
| solution-1-flask   |     0.551081 |       1.00934  |   5.65735  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.524007 |       1.00943  |    4.52865 |
| solution-aron-mark |     0.540013 |       0.149304 |    4.59342 |
| solution-pl        |     0.530874 |       0.147303 |    4.62767 |