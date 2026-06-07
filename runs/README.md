# 2026-06-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.4354   |       1.0562   |   0.105268 |
| solution-1-flask   |     0.443285 |       1.00901  |   0.222669 |
| solution-pl        |     0.443279 |       0.155703 |   0.231323 |
| solution-aron-mark |     0.438948 |       0.157418 |   0.232642 |
| solution-1         |     8.29917  |       1e-06    |   0.662537 |
| solution-2         |     4.93933  |       0.615569 |   1.02603  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.43322  |       0.150344 |   0.345166 |
| solution-pl        |     0.41899  |       0.149683 |   0.363028 |
| solution-flask     |     0.438377 |       1.00892  |   0.397902 |
| solution-1-flask   |     0.424923 |       1.00859  |   0.703764 |
| solution-2         |     0.444601 |       0.510394 |  10.7633   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.439614 |       0.160076 |    1.03329 |
| solution-aron-mark |     0.436033 |       0.160019 |    1.04832 |
| solution-flask     |     0.424837 |       1.00873  |    1.66787 |
| solution-1-flask   |     0.43476  |       1.00899  |    5.63278 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452996 |       0.194736 |    4.00418 |
| solution-aron-mark |     0.430775 |       0.191488 |    4.04457 |
| solution-flask     |     0.445912 |       1.00932  |    5.45124 |