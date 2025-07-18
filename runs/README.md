# 2025-07-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.76155  |       1.10407  |   0.103158 |
| solution-pl        |     0.520589 |       0.1525   |   0.236492 |
| solution-aron-mark |     4.7396   |       0.153327 |   0.239568 |
| solution-1-flask   |     0.523564 |       1.0085   |   0.26833  |
| solution-1         |     8.28629  |       1e-06    |   0.692578 |
| solution-2         |     0.511132 |       0.692953 |   0.78748  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.510617 |       0.155927 |   0.365193 |
| solution-aron-mark |     0.510985 |       0.154219 |   0.367945 |
| solution-flask     |     0.505906 |       1.00839  |   0.378597 |
| solution-1-flask   |     0.518132 |       1.00854  |   0.838804 |
| solution-2         |     0.505496 |       0.536254 |   3.52687  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.511027 |       0.163185 |    1.07002 |
| solution-aron-mark |     0.511619 |       0.163492 |    1.07917 |
| solution-flask     |     0.512924 |       1.00855  |    1.61708 |
| solution-1-flask   |     0.51579  |       1.00856  |    5.7005  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50609  |       0.191628 |    3.23861 |
| solution-aron-mark |     0.507247 |       0.200549 |    3.26011 |
| solution-flask     |     0.511207 |       1.00855  |    5.15329 |