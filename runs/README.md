# 2026-04-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.80861  |       1.04066  |   0.104691 |
| solution-pl        |     4.74392  |       0.148287 |   0.233607 |
| solution-aron-mark |     0.422949 |       0.151868 |   0.234209 |
| solution-1-flask   |     0.43397  |       1.00807  |   0.271541 |
| solution-1         |     8.02169  |       1e-06    |   0.687843 |
| solution-2         |     0.44565  |       0.662791 |   1.04302  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.431746 |       0.148814 |   0.367498 |
| solution-aron-mark |     0.41342  |       0.15122  |   0.373208 |
| solution-flask     |     0.420743 |       1.00818  |   0.395367 |
| solution-1-flask   |     0.421976 |       1.00841  |   0.818368 |
| solution-2         |     0.439652 |       0.519281 |   2.51876  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.418203 |       0.157385 |    1.13495 |
| solution-aron-mark |     0.417793 |       0.153065 |    1.13647 |
| solution-flask     |     0.420018 |       1.00848  |    1.65016 |
| solution-1-flask   |     0.442619 |       1.00884  |    5.799   |
| solution-2         |     0.443278 |       0.571982 |  185.538   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422543 |       0.181354 |    4.00618 |
| solution-aron-mark |     0.417017 |       0.192267 |    4.03496 |
| solution-flask     |     0.423633 |       1.00852  |    5.26227 |