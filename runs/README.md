# 2025-10-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.36532  |       1.05171  |   0.101826 |
| solution-pl        |     0.491513 |       0.15936  |   0.24494  |
| solution-aron-mark |     0.49183  |       0.16162  |   0.245567 |
| solution-1-flask   |     0.505354 |       1.00818  |   0.261891 |
| solution-1         |     7.42991  |       1e-06    |   0.705202 |
| solution-2         |     4.45127  |       0.700135 |   1.52681  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496186 |       0.160982 |   0.37554  |
| solution-aron-mark |     0.493488 |       0.159996 |   0.377063 |
| solution-flask     |     0.490255 |       1.00842  |   0.38133  |
| solution-1-flask   |     0.494811 |       1.0086   |   0.789089 |
| solution-2         |     0.49438  |       0.516201 |   2.64465  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494235 |       0.16916  |    1.09091 |
| solution-aron-mark |     0.496623 |       0.16805  |    1.09679 |
| solution-flask     |     0.499572 |       1.00838  |    1.60075 |
| solution-1-flask   |     0.507676 |       1.00876  |    5.6254  |
| solution-2         |     0.498299 |       0.574596 |   48.7579  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490126 |       0.20157  |    3.41436 |
| solution-aron-mark |     0.492229 |       0.200927 |    3.41752 |
| solution-flask     |     0.497034 |       1.00868  |    5.29301 |