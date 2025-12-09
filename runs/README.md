# 2025-12-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.62319  |       1.06374  |   0.102585 |
| solution-pl        |     0.508272 |       0.176769 |   0.258658 |
| solution-aron-mark |     0.503426 |       0.16956  |   0.260002 |
| solution-1-flask   |     0.513253 |       1.00912  |   0.268618 |
| solution-1         |     7.89567  |       1e-06    |   0.728864 |
| solution-2         |     4.95458  |       0.668478 |   1.35994  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.510331 |       0.172434 |   0.386289 |
| solution-flask     |     0.50808  |       1.00881  |   0.389645 |
| solution-pl        |     0.508389 |       0.178089 |   0.399942 |
| solution-1-flask   |     0.510037 |       1.00945  |   0.821299 |
| solution-2         |     0.501604 |       0.554043 |   5.70449  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504855 |       0.175998 |    1.12538 |
| solution-aron-mark |     0.506549 |       0.182755 |    1.12723 |
| solution-flask     |     0.525563 |       1.0095   |    1.62773 |
| solution-1-flask   |     0.529236 |       1.00933  |    5.92907 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502027 |       0.207542 |    3.96647 |
| solution-aron-mark |     0.51533  |       0.20333  |    3.97015 |
| solution-flask     |     0.516281 |       1.00923  |    5.50329 |