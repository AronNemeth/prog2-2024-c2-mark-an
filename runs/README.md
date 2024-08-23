# 2024-08-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.577985 |       1.00915  |   0.090577 |
| solution-aron-mark |     1.92199  |       0.107762 |   0.176951 |
| solution-pl        |     0.584409 |       0.105278 |   0.184646 |
| solution-1-flask   |     1.28713  |       1.11421  |   0.258223 |
| solution-1         |     7.86139  |       1e-06    |   0.59495  |
| solution-2         |     4.59697  |       0.571718 |   1.30314  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.590744 |       1.00922  |   0.228598 |
| solution-pl        |     0.58483  |       0.108721 |   0.298371 |
| solution-aron-mark |     0.572388 |       0.106974 |   0.302274 |
| solution-1-flask   |     0.586168 |       1.00926  |   0.788428 |
| solution-2         |     0.583366 |       0.491985 |   2.57735  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.573561 |       1.00925  |   0.915701 |
| solution-aron-mark |     0.575335 |       0.11707  |   1.01061  |
| solution-pl        |     0.571428 |       0.115194 |   1.0157   |
| solution-1-flask   |     0.591322 |       1.00911  |   5.43436  |
| solution-2         |     0.569912 |       0.544197 |  40.958    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56912  |       1.00929  |    4.6808  |
| solution-aron-mark |     0.575551 |       0.148236 |    4.81902 |
| solution-pl        |     0.578521 |       0.144502 |    4.86577 |