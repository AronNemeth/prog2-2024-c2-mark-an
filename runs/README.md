# 2024-03-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.56847  |       1.03673  |   0.089056 |
| solution-aron-mark |     0.651616 |       0.110085 |   0.16408  |
| solution-pl        |     0.659063 |       0.110766 |   0.167218 |
| solution-1-flask   |     0.661103 |       1.00835  |   0.269102 |
| solution-2         |     4.78092  |       0.669178 |   0.819628 |
| solution-1         |     8.09253  |       1e-06    |   0.901375 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.655222 |       1.0085   |   0.173894 |
| solution-pl        |     0.655141 |       0.114214 |   0.255949 |
| solution-aron-mark |     0.668563 |       0.115949 |   0.25641  |
| solution-1-flask   |     0.666383 |       1.00855  |   0.795341 |
| solution-2         |     0.659134 |       0.447744 |   2.46563  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.659248 |       0.123023 |   0.800826 |
| solution-pl        |     0.65386  |       0.122038 |   0.803278 |
| solution-flask     |     0.668427 |       1.00867  |   0.924316 |
| solution-1-flask   |     0.667801 |       1.00885  |   5.45328  |
| solution-2         |     0.671573 |       0.500874 | 167.041    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.662993 |       0.153765 |    3.35159 |
| solution-pl        |     0.656045 |       0.152383 |    3.35406 |
| solution-flask     |     0.652945 |       1.00867  |    5.40544 |