# 2024-11-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10643  |       1.08799  |   0.133357 |
| solution-aron-mark |     0.666633 |       0.106974 |   0.17795  |
| solution-pl        |     6.21137  |       0.109196 |   0.180247 |
| solution-1-flask   |     0.567142 |       1.0092   |   0.257566 |
| solution-1         |     8.21918  |       1e-06    |   0.849945 |
| solution-2         |     1.01294  |       0.66967  |   1.02544  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.558006 |       0.108593 |   0.299094 |
| solution-aron-mark |     0.554727 |       0.109622 |   0.323581 |
| solution-flask     |     0.552101 |       1.00889  |   0.496984 |
| solution-1-flask   |     0.565818 |       1.00897  |   0.790085 |
| solution-2         |     0.551933 |       0.474883 |   5.15756  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.552525 |       0.11593  |    1.0271  |
| solution-pl        |     0.552584 |       0.116846 |    1.0299  |
| solution-flask     |     0.556154 |       1.00921  |    2.25699 |
| solution-1-flask   |     0.563547 |       1.00895  |    5.34504 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.557679 |       0.147665 |    4.27373 |
| solution-pl        |     0.554889 |       0.146265 |    4.29231 |
| solution-flask     |     0.549719 |       1.00948  |    8.71502 |