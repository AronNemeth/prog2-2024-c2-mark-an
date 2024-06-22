# 2024-06-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664202 |       1.0088   |   0.073464 |
| solution-aron-mark |     5.86373  |       0.102322 |   0.157304 |
| solution-pl        |     0.657491 |       0.103242 |   0.158561 |
| solution-1-flask   |     1.43327  |       1.10495  |   0.259414 |
| solution-1         |     8.06318  |       1e-06    |   0.573547 |
| solution-2         |     0.65864  |       0.49528  |   1.25676  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672953 |       1.00893  |   0.158679 |
| solution-aron-mark |     0.674186 |       0.104233 |   0.255061 |
| solution-pl        |     0.671752 |       0.105512 |   0.256118 |
| solution-1-flask   |     0.689603 |       1.00895  |   0.777528 |
| solution-2         |     0.663482 |       0.471184 |  12.3999   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665119 |       1.00922  |   0.713865 |
| solution-aron-mark |     0.665452 |       0.113921 |   0.801013 |
| solution-pl        |     0.666959 |       0.11311  |   0.820413 |
| solution-1-flask   |     0.676873 |       1.0091   |   5.47654  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662325 |       1.00905  |    2.50705 |
| solution-pl        |     0.669644 |       0.151662 |    2.61658 |
| solution-aron-mark |     0.664914 |       0.154624 |    2.63637 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657954 |       1.00949  |    15.1362 |
| solution-pl        |     0.669431 |       0.279007 |    20.7019 |
| solution-aron-mark |     0.666039 |       0.276649 |    21.6279 |