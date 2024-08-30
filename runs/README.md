# 2024-08-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563676 |       1.00956  |   0.093641 |
| solution-aron-mark |     1.79354  |       0.110443 |   0.172209 |
| solution-pl        |     0.569451 |       0.103431 |   0.188743 |
| solution-1-flask   |     1.07821  |       1.09925  |   0.258549 |
| solution-1         |     7.62984  |       2e-06    |   0.639315 |
| solution-2         |     4.45453  |       0.568639 |   0.872608 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558609 |       1.00889  |   0.224576 |
| solution-pl        |     0.580064 |       0.107055 |   0.304655 |
| solution-aron-mark |     0.569    |       0.105562 |   0.306933 |
| solution-1-flask   |     0.567941 |       1.00905  |   0.775929 |
| solution-2         |     0.565032 |       0.485757 |   2.05322  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55965  |       1.00913  |   0.901095 |
| solution-pl        |     0.554932 |       0.114179 |   0.99447  |
| solution-aron-mark |     0.561816 |       0.112571 |   0.99957  |
| solution-1-flask   |     0.560967 |       1.00902  |   5.56234  |
| solution-2         |     0.563857 |       0.527256 |  29.3784   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554883 |       1.00939  |    4.20487 |
| solution-pl        |     0.563707 |       0.145031 |    4.27592 |
| solution-aron-mark |     0.560596 |       0.14193  |    4.28163 |