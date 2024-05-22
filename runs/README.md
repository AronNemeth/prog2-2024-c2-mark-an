# 2024-05-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.56867  |       1.07347  |   0.072345 |
| solution-pl        |     0.663952 |       0.100367 |   0.156901 |
| solution-aron-mark |     6.21785  |       0.101297 |   0.157645 |
| solution-1-flask   |     0.677977 |       1.00881  |   0.255346 |
| solution-1         |     8.0718   |       1e-06    |   0.748603 |
| solution-2         |     0.660517 |       0.417763 |   2.13724  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.660528 |       1.00926  |   0.159719 |
| solution-pl        |     0.658621 |       0.108726 |   0.251831 |
| solution-aron-mark |     0.663421 |       0.108936 |   0.255763 |
| solution-1-flask   |     0.674811 |       1.00902  |   0.78986  |
| solution-2         |     0.662892 |       0.429635 |  12.8423   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.666573 |       1.00928  |   0.754344 |
| solution-aron-mark |     0.659599 |       0.114036 |   0.794515 |
| solution-pl        |     0.660126 |       0.114783 |   0.808408 |
| solution-1-flask   |     0.670947 |       1.00913  |   5.5908   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.665751 |       1.00918  |    2.46831 |
| solution-aron-mark |     0.666755 |       0.150237 |    2.58748 |
| solution-pl        |     0.662239 |       0.152071 |    2.60856 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.66586  |       0.270351 |    15.6648 |
| solution-flask     |     0.659747 |       1.00932  |    15.8821 |
| solution-pl        |     0.657778 |       0.270854 |    15.9805 |