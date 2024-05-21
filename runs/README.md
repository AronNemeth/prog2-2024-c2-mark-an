# 2024-05-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.51239  |       1.0921   |   0.068833 |
| solution-pl        |     0.693761 |       0.106368 |   0.163943 |
| solution-aron-mark |     6.20157  |       0.103674 |   0.167408 |
| solution-1-flask   |     0.712674 |       1.00905  |   0.269994 |
| solution-1         |     8.34106  |       1e-06    |   0.743293 |
| solution-2         |     0.683511 |       0.443805 |   0.90148  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.69327  |       1.00951  |   0.164086 |
| solution-aron-mark |     0.695822 |       0.112877 |   0.258787 |
| solution-pl        |     0.681112 |       0.111588 |   0.263779 |
| solution-1-flask   |     0.714478 |       1.00947  |   0.814006 |
| solution-2         |     0.691405 |       0.463716 |   4.52782  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.679666 |       1.00955  |   0.731071 |
| solution-pl        |     0.690675 |       0.117022 |   0.798698 |
| solution-aron-mark |     0.720141 |       0.118662 |   0.811219 |
| solution-1-flask   |     0.694887 |       1.00926  |   5.61252  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67069  |       1.00994  |    2.53595 |
| solution-pl        |     0.692476 |       0.156466 |    2.69163 |
| solution-aron-mark |     0.678501 |       0.158087 |    2.73182 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673212 |       1.00894  |    17.2227 |
| solution-pl        |     0.681829 |       0.275494 |    17.4334 |
| solution-aron-mark |     0.669564 |       0.279812 |    18.3829 |