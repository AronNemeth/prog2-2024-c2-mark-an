# 2024-06-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.48928  |       1.00907  |   0.073498 |
| solution-aron-mark |     5.73413  |       0.102731 |   0.160052 |
| solution-pl        |     0.487034 |       0.1009   |   0.162117 |
| solution-1-flask   |     1.16447  |       1.10973  |   0.260845 |
| solution-1         |     7.79394  |       1e-06    |   0.571423 |
| solution-2         |     0.486176 |       0.506763 |   0.994981 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492546 |       1.00873  |   0.161868 |
| solution-pl        |     0.493361 |       0.103416 |   0.254849 |
| solution-aron-mark |     0.515001 |       0.102772 |   0.26921  |
| solution-1-flask   |     0.501952 |       1.0087   |   0.770551 |
| solution-2         |     0.50043  |       0.467184 |   3.31386  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508616 |       1.00905  |   0.716171 |
| solution-pl        |     0.496449 |       0.112109 |   0.809323 |
| solution-aron-mark |     0.49757  |       0.113026 |   0.810163 |
| solution-1-flask   |     0.499985 |       1.00885  |   5.58627  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.49887  |       1.00931  |    2.562   |
| solution-aron-mark |     0.504504 |       0.165182 |    2.64974 |
| solution-pl        |     0.491649 |       0.149401 |    2.66224 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499784 |       1.00933  |    15.7231 |
| solution-pl        |     0.496073 |       0.275616 |    21.1947 |
| solution-aron-mark |     0.503341 |       0.27181  |    21.3949 |