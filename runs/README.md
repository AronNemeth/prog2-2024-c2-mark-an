# 2026-07-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.13571  |       1.07234  |   0.127326 |
| solution-pl        |     0.457462 |       0.157151 |   0.245939 |
| solution-aron-mark |     0.461511 |       0.158611 |   0.246335 |
| solution-1-flask   |     0.572061 |       1.00873  |   0.265507 |
| solution-1         |     8.06144  |       1e-06    |   0.696979 |
| solution-2         |     5.0196   |       0.682615 |   1.64992  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.457407 |       0.161351 |   0.385659 |
| solution-aron-mark |     0.462431 |       0.160448 |   0.388236 |
| solution-flask     |     0.45909  |       1.00894  |   0.410109 |
| solution-1-flask   |     0.462661 |       1.0087   |   0.824158 |
| solution-2         |     0.456917 |       0.545013 |   7.18954  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.456586 |       0.164112 |    1.14286 |
| solution-pl        |     0.452739 |       0.164921 |    1.14871 |
| solution-flask     |     0.454761 |       1.00892  |    1.73772 |
| solution-1-flask   |     0.464884 |       1.00909  |    5.93145 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.442602 |       0.189929 |    4.2293  |
| solution-aron-mark |     0.464023 |       0.188994 |    4.29761 |
| solution-flask     |     0.452575 |       1.00946  |    5.76196 |