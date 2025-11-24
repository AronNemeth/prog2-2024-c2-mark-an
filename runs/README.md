# 2025-11-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67654  |       1.04562  |   0.101022 |
| solution-aron-mark |     0.466618 |       0.152436 |   0.23768  |
| solution-pl        |     0.463742 |       0.160086 |   0.238003 |
| solution-1-flask   |     0.467966 |       1.00795  |   0.261153 |
| solution-1         |     7.78101  |       1e-06    |   0.675527 |
| solution-2         |     4.72624  |       0.798357 |   0.745756 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.466006 |       0.162417 |   0.357948 |
| solution-pl        |     0.461519 |       0.157302 |   0.366656 |
| solution-flask     |     0.460354 |       1.00806  |   0.369979 |
| solution-1-flask   |     0.466746 |       1.00813  |   0.790362 |
| solution-2         |     0.461205 |       0.496011 |   3.51519  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.462303 |       0.161783 |    1.05034 |
| solution-pl        |     0.46729  |       0.164861 |    1.06036 |
| solution-flask     |     0.465271 |       1.00843  |    1.55749 |
| solution-1-flask   |     0.469623 |       1.00832  |    5.54712 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463267 |       0.191471 |    3.13675 |
| solution-pl        |     0.458485 |       0.191677 |    3.1392  |
| solution-flask     |     0.463432 |       1.00809  |    4.95763 |