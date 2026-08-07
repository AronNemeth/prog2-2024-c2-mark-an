# 2026-08-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.12247  |       1.00877  |   0.097703 |
| solution-1-flask   |     1.36619  |       1.08896  |   0.225735 |
| solution-aron-mark |     0.430647 |       0.152338 |   0.231634 |
| solution-pl        |     0.426581 |       0.154763 |   0.234391 |
| solution-1         |     7.98116  |       1e-06    |   0.604895 |
| solution-2         |     5.00082  |       0.656746 |   1.19699  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.444156 |       0.155466 |   0.3563   |
| solution-pl        |     0.438846 |       0.15822  |   0.357282 |
| solution-flask     |     0.449116 |       1.00936  |   0.387976 |
| solution-1-flask   |     0.447828 |       1.00904  |   0.725675 |
| solution-2         |     0.428474 |       0.501886 |  10.8387   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431108 |       0.162609 |    1.04525 |
| solution-aron-mark |     0.437315 |       0.161676 |    1.04739 |
| solution-flask     |     0.438568 |       1.00924  |    1.64003 |
| solution-1-flask   |     0.450045 |       1.01061  |    5.64853 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429809 |       0.183742 |    3.50263 |
| solution-aron-mark |     0.432981 |       0.188264 |    3.50377 |
| solution-flask     |     0.431977 |       1.00924  |    5.33349 |