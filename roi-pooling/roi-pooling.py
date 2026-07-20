import math
import numpy as np
def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    # Write code here
    feature_map = np.array(feature_map)
    pooled_output = []

    for roi in rois :
        x1,y1,x2,y2 = roi
        roi_h = y2 - y1
        roi_w = x2 - x1

        pooled= np.zeros((output_size, output_size))

        for i in range(output_size) :
            for j in range(output_size) :
                h_start = int(math.floor( y1 + (i * roi_h) /output_size))
                h_end = int(math.floor(y1 + ( (i+1) * roi_h) / output_size))
                w_start = int(math.floor(x1+(j*roi_w)/output_size))
                w_end = int (math.floor(x1 + (j+1)*roi_w/ output_size))

                h_end = max(h_end, h_start+1)
                w_end = max(w_end, w_start+1)

                region = feature_map[h_start:h_end ,w_start:w_end]

                pooled[i,j] = np.max(region)

        pooled_output.append(pooled.tolist())

    return pooled_output
    pass