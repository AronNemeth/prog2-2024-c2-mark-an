# 2025-10-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4154   |       1.05867  |   0.099092 |
| solution-pl        |     0.48288  |       0.154527 |   0.237428 |
| solution-aron-mark |     0.486209 |       0.154828 |   0.239213 |
| solution-1-flask   |     0.48627  |       1.00814  |   0.26443  |
| solution-1         |     7.53618  |       1e-06    |   0.711972 |
| solution-2         |     4.41813  |       0.724642 |   1.40321  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48634  |       0.154793 |   0.362236 |
| solution-pl        |     0.483736 |       0.155165 |   0.366395 |
| solution-flask     |     0.486844 |       1.0084   |   0.376757 |
| solution-1-flask   |     0.484611 |       1.00841  |   0.799209 |
| solution-2         |     0.480284 |       0.501951 |   2.97502  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486821 |       0.170429 |    1.082   |
| solution-pl        |     0.48269  |       0.181261 |    1.10316 |
| solution-flask     |     0.501889 |       1.00891  |    1.57273 |
| solution-1-flask   |     0.507661 |       1.00837  |    5.69266 |
| solution-2         |     0.480172 |       0.556759 |  434.607   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.503561 |       0.198692 |    3.25568 |
| solution-aron-mark |     0.487183 |       0.193638 |    3.51211 |
| solution-flask     |     0.528091 |       1.00866  |    5.34581 |