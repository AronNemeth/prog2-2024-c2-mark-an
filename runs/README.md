# 2024-07-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.16267  |       1.09146  |   0.095862 |
| solution-pl        |     5.80055  |       0.102939 |   0.167646 |
| solution-aron-mark |     0.496212 |       0.100466 |   0.168633 |
| solution-1-flask   |     0.506951 |       1.00905  |   0.258859 |
| solution-1         |     7.94152  |       1e-06    |   0.744639 |
| solution-2         |     0.507014 |       0.586935 |   0.97581  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.49926  |       1.00912  |   0.222983 |
| solution-aron-mark |     0.499215 |       0.102505 |   0.285786 |
| solution-pl        |     0.496705 |       0.106199 |   0.293295 |
| solution-1-flask   |     0.516008 |       1.00878  |   0.78689  |
| solution-2         |     0.496793 |       0.479709 |   5.50608  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500948 |        1.00884 |   0.885048 |
| solution-aron-mark |     0.502927 |        0.11237 |   0.987932 |
| solution-pl        |     0.506121 |        0.11159 |   0.991824 |
| solution-1-flask   |     0.508597 |        1.00917 |   5.6636   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499499 |       1.00936  |    4.09094 |
| solution-aron-mark |     0.504803 |       0.14761  |    4.14809 |
| solution-pl        |     0.505059 |       0.150409 |    4.23978 |