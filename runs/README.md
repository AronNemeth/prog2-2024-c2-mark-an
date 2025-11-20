# 2025-11-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.58881  |       1.1253   |   0.102365 |
| solution-pl        |     0.493111 |       0.161689 |   0.249204 |
| solution-aron-mark |     0.484861 |       0.16357  |   0.261125 |
| solution-1-flask   |     0.509672 |       1.00868  |   0.276916 |
| solution-1         |     7.74636  |       1e-06    |   0.765924 |
| solution-2         |     4.70107  |       0.682604 |   1.03355  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481371 |       0.164264 |   0.368042 |
| solution-aron-mark |     0.481604 |       0.162546 |   0.371011 |
| solution-flask     |     0.481454 |       1.00874  |   0.379087 |
| solution-1-flask   |     0.484777 |       1.00845  |   0.799074 |
| solution-2         |     0.47958  |       0.524492 |   3.76168  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495009 |       0.169935 |    1.07308 |
| solution-pl        |     0.492516 |       0.173318 |    1.08505 |
| solution-flask     |     0.475407 |       1.00845  |    1.62372 |
| solution-1-flask   |     0.484061 |       1.00883  |    5.65277 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485423 |       0.19992  |    3.30151 |
| solution-pl        |     0.487068 |       0.200488 |    3.34063 |
| solution-flask     |     0.484272 |       1.00855  |    5.26498 |