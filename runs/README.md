# 2026-03-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.58196  |       1.09115  |   0.107949 |
| solution-aron-mark |     0.466698 |       0.151946 |   0.24388  |
| solution-pl        |     4.84386  |       0.152755 |   0.252289 |
| solution-1-flask   |     0.459723 |       1.00878  |   0.262195 |
| solution-1         |     7.74677  |       1e-06    |   0.612031 |
| solution-2         |     0.476158 |       0.558207 |   1.55535  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.483322 |       0.154051 |   0.38231  |
| solution-aron-mark |     0.482278 |       0.155212 |   0.384382 |
| solution-flask     |     0.488638 |       1.00972  |   0.396467 |
| solution-1-flask   |     0.472858 |       1.00922  |   0.841177 |
| solution-2         |     0.47673  |       0.530602 |   2.74426  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474789 |       0.155874 |    1.13939 |
| solution-pl        |     0.459621 |       0.163626 |    1.17311 |
| solution-flask     |     0.502364 |       1.00906  |    1.65927 |
| solution-1-flask   |     0.467148 |       1.00877  |    5.70615 |
| solution-2         |     0.466925 |       0.592294 |  170.975   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451003 |       0.191552 |    3.94945 |
| solution-aron-mark |     0.465676 |       0.18167  |    4.06798 |
| solution-flask     |     0.455988 |       1.00893  |    5.25353 |