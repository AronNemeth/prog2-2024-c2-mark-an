# 2026-02-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.10052  |       1.10885  |   0.107301 |
| solution-pl        |     4.73384  |       0.149138 |   0.234593 |
| solution-aron-mark |     0.449523 |       0.146678 |   0.23741  |
| solution-1-flask   |     0.454412 |       1.00841  |   0.268331 |
| solution-1         |     8.18983  |       1e-06    |   1.03108  |
| solution-2         |     0.453441 |       0.890225 |   1.09925  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.454853 |       0.150522 |   0.369382 |
| solution-aron-mark |     0.457891 |       0.152174 |   0.369723 |
| solution-flask     |     0.446257 |       1.00871  |   0.391341 |
| solution-1-flask   |     0.457612 |       1.00873  |   0.799157 |
| solution-2         |     0.452922 |       0.537333 |   2.31319  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.459948 |       0.154541 |    1.14218 |
| solution-aron-mark |     0.449601 |       0.153287 |    1.16095 |
| solution-flask     |     0.45526  |       1.00896  |    1.65856 |
| solution-1-flask   |     0.460436 |       1.00877  |    5.66973 |
| solution-2         |     0.445014 |       0.571734 |   32.7736  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.448956 |       0.177248 |    3.9425  |
| solution-aron-mark |     0.451238 |       0.180845 |    3.96164 |
| solution-flask     |     0.448215 |       1.00897  |    5.20028 |