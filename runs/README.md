# 2025-12-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73144  |       1.09231  |   0.107858 |
| solution-pl        |     0.529454 |       0.176087 |   0.261234 |
| solution-aron-mark |     0.528377 |       0.181111 |   0.263374 |
| solution-1-flask   |     0.540318 |       1.01369  |   0.27755  |
| solution-1         |     8.42071  |       2e-06    |   0.687792 |
| solution-2         |     4.76109  |       0.70323  |   1.10363  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521461 |       1.00895  |   0.398566 |
| solution-aron-mark |     0.526219 |       0.181679 |   0.429513 |
| solution-pl        |     0.525999 |       0.184709 |   0.433734 |
| solution-1-flask   |     0.545466 |       1.00924  |   0.862621 |
| solution-2         |     0.524892 |       0.605734 |   2.36131  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.519423 |       0.181628 |    1.10202 |
| solution-aron-mark |     0.517693 |       0.179723 |    1.1081  |
| solution-flask     |     0.509031 |       1.00882  |    1.65838 |
| solution-1-flask   |     0.52748  |       1.00913  |    6.13202 |
| solution-2         |     0.533937 |       0.663856 |   58.9803  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505249 |       0.210674 |    3.66241 |
| solution-pl        |     0.510618 |       0.209847 |    3.68273 |
| solution-flask     |     0.521803 |       1.00928  |    5.4613  |