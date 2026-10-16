# 2026-10-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.942078 |       1.04906  |   0.051758 |
| solution-1-flask   |     0.281732 |       1.00733  |   0.124577 |
| solution-aron-mark |     4.53962  |       0.50631  |   0.145214 |
| solution-pl        |     0.277142 |       0.105027 |   0.146898 |
| solution-1         |     5.55666  |       1e-06    |   0.373634 |
| solution-2         |     0.281262 |       0.48807  |   0.861139 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.297248 |       1.00757  |   0.105807 |
| solution-pl        |     0.285277 |       0.108316 |   0.21612  |
| solution-aron-mark |     0.274364 |       0.110443 |   0.236428 |
| solution-1-flask   |     0.287328 |       1.01168  |   0.373839 |
| solution-2         |     0.332608 |       0.375122 |   2.15682  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.322693 |       1.00796  |   0.512739 |
| solution-aron-mark |     0.290551 |       0.120163 |   0.583119 |
| solution-pl        |     0.318236 |       0.133208 |   0.592772 |
| solution-1-flask   |     0.311249 |       1.00751  |   3.13604  |
| solution-2         |     0.279979 |       0.387203 |  94.6037   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.335601 |       0.14315  |    2.11089 |
| solution-aron-mark |     0.351709 |       0.157269 |    2.17576 |
| solution-flask     |     0.382485 |       1.00815  |    2.65945 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.368731 |       0.20188  |    14.384  |
| solution-pl        |     0.294288 |       0.604108 |    14.8608 |
| solution-flask     |     0.303632 |       1.0075   |    17.6381 |