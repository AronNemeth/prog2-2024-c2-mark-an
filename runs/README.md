# 2025-02-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.1414   |       1.05512  |   0.077926 |
| solution-pl        |     4.35696  |       0.137255 |   0.19309  |
| solution-aron-mark |     0.518492 |       0.137793 |   0.200431 |
| solution-1-flask   |     0.527887 |       1.00842  |   0.260974 |
| solution-1         |     6.99024  |       1e-06    |   0.579704 |
| solution-2         |     0.515139 |       0.553147 |   1.05743  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.523275 |       1.00808  |   0.279871 |
| solution-aron-mark |     0.527004 |       0.140767 |   0.299792 |
| solution-pl        |     0.521666 |       0.140037 |   0.300971 |
| solution-1-flask   |     0.526476 |       1.00883  |   0.776775 |
| solution-2         |     0.511764 |       0.47911  |   4.28866  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524063 |       0.146564 |   0.873055 |
| solution-aron-mark |     0.525873 |       0.145653 |   0.886923 |
| solution-flask     |     0.535625 |       1.00882  |   1.20691  |
| solution-1-flask   |     0.524192 |       1.0084   |   5.54637  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530485 |       0.173923 |    2.7462  |
| solution-pl        |     0.527454 |       0.172423 |    2.76709 |
| solution-flask     |     0.519259 |       1.00919  |    4.05074 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.510822 |       0.273303 |    15.7787 |
| solution-pl        |     0.525143 |       0.272032 |    15.8322 |