# 2026-06-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.25331  |       1.06814  |   0.105343 |
| solution-pl        |     6.06023  |       0.153198 |   0.214018 |
| solution-aron-mark |     0.392355 |       0.141664 |   0.214895 |
| solution-1-flask   |     0.402227 |       1.00668  |   0.232118 |
| solution-1         |     6.99284  |       1e-06    |   0.557163 |
| solution-2         |     0.395021 |       0.595329 |   1.0541   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443176 |       0.140882 |   0.3317   |
| solution-pl        |     0.399875 |       0.142306 |   0.33421  |
| solution-flask     |     0.393082 |       1.00669  |   0.434546 |
| solution-1-flask   |     0.399055 |       1.00707  |   0.727012 |
| solution-2         |     0.399509 |       0.500243 |   2.15708  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.390922 |       0.149498 |    1.01156 |
| solution-pl        |     0.397251 |       0.145721 |    1.0414  |
| solution-flask     |     0.396188 |       1.007    |    1.82652 |
| solution-1-flask   |     0.408205 |       1.00769  |    5.4032  |
| solution-2         |     0.39718  |       0.531261 |  158.816   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.394222 |       0.174328 |    4.80687 |
| solution-pl        |     0.398725 |       0.175131 |    4.80908 |
| solution-flask     |     0.392708 |       1.00704  |    6.00132 |