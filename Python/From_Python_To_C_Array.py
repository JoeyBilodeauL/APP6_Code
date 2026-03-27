import numpy as np

Q2_13_SCALE = 2 ** 13  # 8192

def array_to_txt(arr, size=None, output_file="output.txt"):
    arr = np.asarray(arr).flatten()[:size]
    arr_fixed = (arr * Q2_13_SCALE).astype(np.int32)  # convert to Q2.13
    with open(output_file, "w") as f:
        for v in arr_fixed:
            f.write(str(v) + ",\n")