# 2025-02-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.522738 |       1.00857  |   0.081029 |
| solution-aron-mark |     0.527976 |       0.139822 |   0.201535 |
| solution-pl        |     1.95215  |       0.148482 |   0.203385 |
| solution-1-flask   |     5.34452  |       1.09654  |   0.264473 |
| solution-1         |     7.51827  |       1e-06    |   0.596359 |
| solution-2         |     0.523543 |       0.574996 |   1.22991  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.532487 |       1.00864  |   0.288721 |
| solution-pl        |     0.525872 |       0.141302 |   0.302937 |
| solution-aron-mark |     0.525354 |       0.164253 |   0.311349 |
| solution-1-flask   |     0.536556 |       1.00881  |   0.795674 |
| solution-2         |     0.525148 |       0.496978 |   2.74011  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525347 |       0.148092 |   0.905071 |
| solution-aron-mark |     0.527967 |       0.148007 |   0.917601 |
| solution-flask     |     0.526402 |       1.00941  |   1.24353  |
| solution-1-flask   |     0.533436 |       1.00875  |   5.69645  |
| solution-2         |     0.530914 |       0.550114 |  46.4401   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.524445 |       0.175931 |    2.80338 |
| solution-pl        |     0.527725 |       0.174642 |    2.84246 |
| solution-flask     |     0.527289 |       1.00897  |    4.18498 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525626 |       0.280571 |    16.414  |
| solution-pl        |     0.52735  |       0.277364 |    16.7453 |