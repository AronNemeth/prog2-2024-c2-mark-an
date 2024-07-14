# 2024-07-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.0574   |       1.0498   |   0.094426 |
| solution-pl        |     5.71701  |       0.101837 |   0.164166 |
| solution-aron-mark |     0.493483 |       0.100088 |   0.165684 |
| solution-1-flask   |     0.510994 |       1.00879  |   0.254271 |
| solution-1         |     7.75233  |       1e-06    |   0.646012 |
| solution-2         |     0.506129 |       0.599956 |   1.4059   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492037 |       1.009    |   0.219022 |
| solution-aron-mark |     0.492908 |       0.105601 |   0.280981 |
| solution-pl        |     0.49299  |       0.102673 |   0.284448 |
| solution-1-flask   |     0.502779 |       1.00937  |   0.761155 |
| solution-2         |     0.490099 |       0.466016 |   7.58824  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.490496 |       1.00899  |   0.883938 |
| solution-aron-mark |     0.497492 |       0.111212 |   0.973907 |
| solution-pl        |     0.492887 |       0.111088 |   0.976946 |
| solution-1-flask   |     0.501064 |       1.00867  |   5.59432  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.491439 |       1.00907  |    4.03677 |
| solution-aron-mark |     0.488326 |       0.146492 |    4.15114 |
| solution-pl        |     0.497015 |       0.148252 |    4.18289 |