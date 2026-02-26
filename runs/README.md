# 2026-02-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.97255  |       1.05057  |   0.107274 |
| solution-pl        |     4.86501  |       0.148043 |   0.234345 |
| solution-aron-mark |     0.455708 |       0.147604 |   0.238193 |
| solution-1-flask   |     0.460364 |       1.00879  |   0.271422 |
| solution-1         |     8.25826  |       1e-06    |   0.779672 |
| solution-2         |     0.456979 |       0.751323 |   0.925953 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.459626 |       0.148604 |   0.369523 |
| solution-aron-mark |     0.453259 |       0.149634 |   0.375588 |
| solution-flask     |     0.460373 |       1.00897  |   0.390773 |
| solution-1-flask   |     0.467177 |       1.00878  |   0.79349  |
| solution-2         |     0.447953 |       0.524903 |  11.3734   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452949 |       0.155246 |    1.12305 |
| solution-aron-mark |     0.457389 |       0.155086 |    1.12878 |
| solution-flask     |     0.461582 |       1.00894  |    1.66074 |
| solution-1-flask   |     0.460887 |       1.00933  |    5.59603 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.458138 |       0.181088 |    3.944   |
| solution-pl        |     0.46869  |       0.180312 |    4.00328 |
| solution-flask     |     0.452651 |       1.009    |    5.30911 |