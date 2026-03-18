# 2026-03-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.13613  |       1.0718   |   0.107766 |
| solution-aron-mark |     0.466881 |       0.15179  |   0.2421   |
| solution-pl        |     4.97772  |       0.156456 |   0.242758 |
| solution-1-flask   |     0.47653  |       1.00897  |   0.271618 |
| solution-1         |     8.38158  |       1e-06    |   0.730974 |
| solution-2         |     0.465153 |       0.721688 |   1.05687  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.471366 |       0.157972 |   0.375418 |
| solution-pl        |     0.463732 |       0.155664 |   0.378422 |
| solution-flask     |     0.466089 |       1.00912  |   0.402361 |
| solution-1-flask   |     0.472193 |       1.00905  |   0.817542 |
| solution-2         |     0.451327 |       0.513449 |   2.21855  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464985 |       0.157945 |    1.11711 |
| solution-aron-mark |     0.465771 |       0.174824 |    1.12727 |
| solution-flask     |     0.453293 |       1.00893  |    1.62624 |
| solution-1-flask   |     0.466587 |       1.00907  |    5.76981 |
| solution-2         |     0.469001 |       0.614584 |   40.5365  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.467618 |       0.192364 |    4.08415 |
| solution-aron-mark |     0.460134 |       0.188359 |    4.163   |
| solution-flask     |     0.466402 |       1.0091   |    5.3771  |