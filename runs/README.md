# 2024-06-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.40955  |       1.12966  |   0.076388 |
| solution-aron-mark |     5.89301  |       0.101608 |   0.159728 |
| solution-pl        |     0.660518 |       0.104767 |   0.161226 |
| solution-1-flask   |     0.685907 |       1.00925  |   0.261445 |
| solution-1         |     7.98531  |       1e-06    |   0.657558 |
| solution-2         |     0.656228 |       0.421702 |   1.17386  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666854 |       1.009    |   0.165085 |
| solution-aron-mark |     0.665797 |       0.108114 |   0.263259 |
| solution-pl        |     0.660506 |       0.102916 |   0.267902 |
| solution-1-flask   |     0.697256 |       1.00891  |   0.792949 |
| solution-2         |     0.666926 |       0.430919 |   1.87311  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668074 |       1.00917  |   0.73643  |
| solution-pl        |     0.662233 |       0.111421 |   0.814392 |
| solution-aron-mark |     0.680376 |       0.115725 |   0.815973 |
| solution-1-flask   |     0.67989  |       1.00848  |   5.5644   |
| solution-2         |     0.686151 |       0.497216 | 169.351    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.6638   |       1.00962  |    2.4948  |
| solution-pl        |     0.670679 |       0.150872 |    2.62349 |
| solution-aron-mark |     0.672493 |       0.149318 |    2.64112 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.65375  |       1.00866  |    15.8738 |
| solution-aron-mark |     0.678238 |       0.278214 |    21.9834 |
| solution-pl        |     0.665767 |       0.277391 |    22.1343 |