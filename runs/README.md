# 2024-04-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672318 |       1.00882  |   0.065721 |
| solution-aron-mark |     0.667018 |       0.113331 |   0.168278 |
| solution-pl        |     6.00385  |       0.112044 |   0.168586 |
| solution-1-flask   |     1.45969  |       1.04529  |   0.262963 |
| solution-1         |     8.20343  |       1e-06    |   0.591657 |
| solution-2         |     0.667017 |       0.412748 |   1.05967  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667674 |       1.00891  |   0.172813 |
| solution-aron-mark |     0.66227  |       0.115688 |   0.257392 |
| solution-pl        |     0.668751 |       0.114913 |   0.258559 |
| solution-1-flask   |     0.683768 |       1.0087   |   0.797034 |
| solution-2         |     0.668502 |       0.433944 |   2.18079  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.675096 |       0.121658 |   0.820851 |
| solution-aron-mark |     0.658232 |       0.121121 |   0.822139 |
| solution-flask     |     0.659211 |       1.00881  |   0.927926 |
| solution-1-flask   |     0.67524  |       1.00889  |   5.56539  |
| solution-2         |     0.668454 |       0.48646  |  41.8101   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.663813 |       0.154295 |    3.27596 |
| solution-pl        |     0.667381 |       0.153332 |    3.29574 |
| solution-flask     |     0.666832 |       1.00884  |    5.28461 |