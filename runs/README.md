# 2025-09-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.488578 |       1.00835  |   0.101531 |
| solution-pl        |     5.79995  |       0.289432 |   0.241012 |
| solution-aron-mark |     0.488595 |       0.156804 |   0.243196 |
| solution-1-flask   |     1.0948   |       1.04472  |   0.268597 |
| solution-1         |     7.56177  |       1e-06    |   0.741376 |
| solution-2         |     0.488616 |       0.684174 |   0.856096 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484043 |       0.154714 |   0.367613 |
| solution-aron-mark |     0.492266 |       0.157111 |   0.370609 |
| solution-flask     |     0.485639 |       1.00852  |   0.379361 |
| solution-1-flask   |     0.496805 |       1.00843  |   0.793406 |
| solution-2         |     0.494613 |       0.510478 |   8.09662  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484877 |       0.162277 |    1.05841 |
| solution-aron-mark |     0.484037 |       0.162239 |    1.06927 |
| solution-flask     |     0.488875 |       1.0087   |    1.60209 |
| solution-1-flask   |     0.492953 |       1.00864  |    5.62144 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.490874 |       0.194044 |    3.30994 |
| solution-pl        |     0.489466 |       0.192212 |    3.33249 |
| solution-flask     |     0.485627 |       1.00857  |    5.22107 |