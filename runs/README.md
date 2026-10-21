# 2026-10-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.86438  |       1.08404  |   0.107533 |
| solution-aron-mark |     5.38559  |       0.175776 |   0.25707  |
| solution-pl        |     0.44963  |       0.172334 |   0.258925 |
| solution-1-flask   |     0.468767 |       1.00864  |   0.269925 |
| solution-1         |     8.89549  |       1e-06    |   0.598313 |
| solution-2         |     0.442322 |       0.558152 |   0.811513 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.445987 |       1.00893  |   0.234028 |
| solution-pl        |     0.445101 |       0.171225 |   0.388572 |
| solution-aron-mark |     0.441921 |       0.171682 |   0.392914 |
| solution-1-flask   |     0.449264 |       1.0092   |   0.794801 |
| solution-2         |     0.467782 |       0.534583 |   2.23281  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.454419 |       1.00877  |    1.009   |
| solution-pl        |     0.435071 |       0.184038 |    1.14176 |
| solution-aron-mark |     0.447903 |       0.181304 |    1.15777 |
| solution-1-flask   |     0.452671 |       1.00887  |    5.53833 |
| solution-2         |     0.443115 |       0.580558 |  289.724   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447363 |       0.215678 |    3.62142 |
| solution-pl        |     0.470837 |       0.216432 |    3.68842 |
| solution-flask     |     0.446281 |       1.00901  |    4.45719 |