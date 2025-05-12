# 2025-05-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.460451 |       1.00884  |   0.08354  |
| solution-pl        |     0.46849  |       0.122704 |   0.192028 |
| solution-aron-mark |     2.27233  |       0.121948 |   0.196639 |
| solution-1-flask   |     1.55433  |       1.06511  |   0.305575 |
| solution-1         |     8.03884  |       1e-06    |   0.725162 |
| solution-2         |     4.97742  |       0.687951 |   0.784539 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465669 |       0.121065 |   0.293635 |
| solution-pl        |     0.466523 |       0.121534 |   0.297    |
| solution-flask     |     0.457676 |       1.00936  |   0.298137 |
| solution-1-flask   |     0.470235 |       1.00885  |   0.78666  |
| solution-2         |     0.469933 |       0.508824 |   2.74956  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481751 |       0.134121 |   0.883375 |
| solution-pl        |     0.480869 |       0.131734 |   0.908657 |
| solution-flask     |     0.478086 |       1.00904  |   1.2797   |
| solution-1-flask   |     0.480026 |       1.00935  |   5.47871  |
| solution-2         |     0.46076  |       0.555454 |  46.0782   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482944 |       0.169295 |    2.86839 |
| solution-aron-mark |     0.478543 |       0.162748 |    3.00735 |
| solution-flask     |     0.477251 |       1.00917  |    4.37629 |

## Inputs: 1000000, Queries 1000

| solution    |   setup_time |   preproc_time |   run_time |
|:------------|-------------:|---------------:|-----------:|
| solution-pl |      0.48156 |       0.266632 |    16.8159 |