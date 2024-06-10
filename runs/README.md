# 2024-06-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.70175  |       1.07058  |   0.077108 |
| solution-aron-mark |     6.35758  |       0.10519  |   0.162464 |
| solution-pl        |     0.681458 |       0.106047 |   0.165937 |
| solution-1-flask   |     0.703178 |       1.00901  |   0.263892 |
| solution-1         |     8.72789  |       1e-06    |   0.6212   |
| solution-2         |     0.675018 |       0.448783 |   0.969597 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.698903 |       1.00912  |   0.166959 |
| solution-aron-mark |     0.69106  |       0.108356 |   0.261342 |
| solution-pl        |     0.703498 |       0.109669 |   0.262841 |
| solution-1-flask   |     0.726959 |       1.00902  |   0.795925 |
| solution-2         |     0.695409 |       0.450752 |   2.92966  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.703956 |       1.0092   |   0.718767 |
| solution-aron-mark |     0.695009 |       0.115316 |   0.804076 |
| solution-pl        |     0.72142  |       0.116459 |   0.812802 |
| solution-1-flask   |     0.763684 |       1.00913  |   5.83614  |
| solution-2         |     0.680959 |       0.51468  | 176.849    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.682401 |       1.00973  |    2.63016 |
| solution-aron-mark |     0.708118 |       0.152809 |    2.73087 |
| solution-pl        |     0.69241  |       0.155499 |    2.75749 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.691657 |       1.00927  |    16.9365 |
| solution-pl        |     0.686105 |       0.282564 |    22.2738 |
| solution-aron-mark |     0.693478 |       0.283676 |    23.4238 |