# 2026-09-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.50868  |       1.04108  |   0.100567 |
| solution-aron-mark |     0.405057 |       0.144692 |   0.220897 |
| solution-pl        |     2.91019  |       0.157137 |   0.222521 |
| solution-1-flask   |     0.413567 |       1.00695  |   0.24397  |
| solution-1         |     7.73251  |       2e-06    |   0.633203 |
| solution-2         |     5.20192  |       0.600584 |   0.758704 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.408687 |       0.151127 |   0.330433 |
| solution-pl        |     0.409928 |       0.151167 |   0.356551 |
| solution-flask     |     0.403805 |       1.01089  |   0.436939 |
| solution-1-flask   |     0.405437 |       1.0069   |   0.722723 |
| solution-2         |     0.400981 |       0.498953 |  13.5412   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.400841 |       0.151434 |    1.04782 |
| solution-aron-mark |     0.403595 |       0.152309 |    1.05093 |
| solution-flask     |     0.401888 |       1.00729  |    1.80833 |
| solution-1-flask   |     0.40609  |       1.00754  |    5.48398 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.403939 |       0.182864 |    4.52144 |
| solution-aron-mark |     0.410721 |       0.180748 |    4.54493 |
| solution-flask     |     0.402989 |       1.00789  |    6.03787 |