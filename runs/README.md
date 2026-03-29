# 2026-03-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.07651  |       1.03613  |   0.105172 |
| solution-aron-mark |     0.444336 |       0.154229 |   0.239885 |
| solution-pl        |     4.90883  |       0.154637 |   0.246211 |
| solution-1-flask   |     0.454486 |       1.0084   |   0.273443 |
| solution-1         |     9.55205  |       1e-06    |   0.755816 |
| solution-2         |     0.436786 |       0.71892  |   0.957716 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438961 |       0.154228 |   0.367906 |
| solution-pl        |     0.444966 |       0.157335 |   0.377102 |
| solution-flask     |     0.439725 |       1.00884  |   0.394781 |
| solution-1-flask   |     0.448414 |       1.0093   |   0.820174 |
| solution-2         |     0.434268 |       0.555622 |   4.93697  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.454293 |       0.164744 |    1.10577 |
| solution-pl        |     0.442732 |       0.159056 |    1.11082 |
| solution-flask     |     0.438713 |       1.00854  |    1.64625 |
| solution-1-flask   |     0.45213  |       1.00917  |    5.83179 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.453887 |       0.188527 |    4.18898 |
| solution-pl        |     0.443642 |       0.186179 |    4.28723 |
| solution-flask     |     0.438442 |       1.00921  |    5.47222 |