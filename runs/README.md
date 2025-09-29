# 2025-09-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73161  |       1.08207  |   0.105517 |
| solution-aron-mark |     0.502277 |       0.163719 |   0.244182 |
| solution-pl        |     0.496083 |       0.157716 |   0.244322 |
| solution-1-flask   |     0.498697 |       1.00808  |   0.277005 |
| solution-1         |     8.39955  |       1e-06    |   0.676183 |
| solution-2         |     4.70283  |       0.710925 |   1.02453  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48733  |       0.156332 |   0.366055 |
| solution-aron-mark |     0.49654  |       0.156221 |   0.36825  |
| solution-flask     |     0.489777 |       1.00837  |   0.375679 |
| solution-1-flask   |     0.490445 |       1.00833  |   0.807586 |
| solution-2         |     0.502464 |       0.540513 |   5.21159  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.483768 |       0.163829 |    1.0696  |
| solution-pl        |     0.492832 |       0.16549  |    1.07544 |
| solution-flask     |     0.483865 |       1.00842  |    1.59396 |
| solution-1-flask   |     0.513871 |       1.00848  |    5.69305 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494666 |       0.19481  |    3.31122 |
| solution-pl        |     0.492074 |       0.191773 |    3.31387 |
| solution-flask     |     0.487666 |       1.0088   |    5.20096 |