# 2024-12-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.78192  |       1.00867  |   0.102546 |
| solution-pl        |     0.524419 |       0.109194 |   0.18543  |
| solution-aron-mark |     0.523754 |       0.107656 |   0.186283 |
| solution-1-flask   |     4.60639  |       1.11666  |   0.270462 |
| solution-1         |     7.20166  |       1e-06    |   0.582409 |
| solution-2         |     0.525707 |       0.478    |   0.916419 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.538001 |       0.110238 |   0.313987 |
| solution-pl        |     0.536782 |       0.112959 |   0.315707 |
| solution-flask     |     0.527184 |       1.00832  |   0.478279 |
| solution-1-flask   |     0.526835 |       1.00854  |   0.794774 |
| solution-2         |     0.536576 |       0.469573 |   2.15325  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525649 |       0.116418 |    1.07374 |
| solution-aron-mark |     0.525505 |       0.117216 |    1.07402 |
| solution-flask     |     0.544583 |       1.00872  |    2.16619 |
| solution-1-flask   |     0.532273 |       1.00883  |    5.85613 |
| solution-2         |     0.524404 |       0.518777 |   31.8834  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.533872 |       0.148069 |    4.38627 |
| solution-aron-mark |     0.54343  |       0.145218 |    4.60048 |
| solution-flask     |     0.527627 |       1.0091   |    8.55309 |