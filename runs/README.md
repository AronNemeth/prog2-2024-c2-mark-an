# 2025-07-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1923   |       1.10549  |   0.105172 |
| solution-aron-mark |     5.93211  |       0.182885 |   0.234018 |
| solution-pl        |     0.486271 |       0.148854 |   0.236693 |
| solution-1-flask   |     0.501303 |       1.00806  |   0.269185 |
| solution-1         |     7.75892  |       1e-06    |   0.66274  |
| solution-2         |     0.502951 |       0.64893  |   0.927906 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.503164 |       0.151576 |   0.362576 |
| solution-aron-mark |     0.499892 |       0.150178 |   0.368136 |
| solution-flask     |     0.503873 |       1.00826  |   0.381937 |
| solution-1-flask   |     0.505857 |       1.00828  |   0.80799  |
| solution-2         |     0.496227 |       0.503273 |   2.71333  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.50511  |       0.156776 |    1.07024 |
| solution-aron-mark |     0.500572 |       0.15763  |    1.07057 |
| solution-flask     |     0.510737 |       1.00865  |    1.59937 |
| solution-1-flask   |     0.512319 |       1.00831  |    5.69688 |
| solution-2         |     0.500689 |       0.556239 |  299.946   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506013 |       0.189669 |    3.21847 |
| solution-pl        |     0.498733 |       0.187979 |    3.24194 |
| solution-flask     |     0.505641 |       1.00835  |    5.13171 |