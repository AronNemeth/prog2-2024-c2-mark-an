# 2024-05-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.33727  |       1.05549  |   0.077119 |
| solution-aron-mark |     5.85125  |       0.102085 |   0.157745 |
| solution-pl        |     0.655635 |       0.103106 |   0.158283 |
| solution-1-flask   |     0.68264  |       1.00903  |   0.253365 |
| solution-1         |     7.91345  |       1e-06    |   0.754861 |
| solution-2         |     0.653164 |       0.412606 |   1.57078  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.656898 |       1.00884  |   0.161644 |
| solution-aron-mark |     0.6588   |       0.103198 |   0.257285 |
| solution-pl        |     0.662227 |       0.102679 |   0.260371 |
| solution-1-flask   |     0.671688 |       1.00934  |   0.797188 |
| solution-2         |     0.659601 |       0.425136 |   2.51833  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666462 |       1.00924  |   0.716821 |
| solution-pl        |     0.66527  |       0.110659 |   0.798939 |
| solution-aron-mark |     0.659199 |       0.111884 |   0.808669 |
| solution-1-flask   |     0.68146  |       1.00915  |   5.65238  |
| solution-2         |     0.668083 |       0.483875 |  29.7777   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674504 |       1.00963  |    2.62689 |
| solution-aron-mark |     0.67691  |       0.151037 |    2.65224 |
| solution-pl        |     0.673152 |       0.154287 |    2.773   |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658277 |       1.00909  |    16.4519 |
| solution-pl        |     0.686712 |       0.276656 |    22.8458 |
| solution-aron-mark |     0.699277 |       0.275043 |    23.6564 |